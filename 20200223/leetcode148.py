'''
148. 链表排序
'''
# 归并实现
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        def merge(left, right):
            res = pNode = ListNode(0)
            while left and right:
                if left.val < right.val:
                    pNode.next = left
                    left = left.next
                else:
                    pNode.next = right
                    right = right.next
                pNode = pNode.next
            pNode.next = left if left else right
            return res.next

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        left = self.sortList(head)
        right = self.sortList(mid)
        return merge(left, right)

# 快排实现（超出时间限制？）
class Solution2:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        def partition(begin, end):
            pivot = p1 = begin
            p2 = p1.next
            while p2 != end:
                if p2.val < pivot.val:
                    p1 = p1.next
                    tmp = p2.val
                    p2.val = p1.val
                    p1.val = tmp
                p2 = p2.next
            tmp = pivot.val
            pivot.val = p1.val
            p1.val = tmp
            return p1

        def quickSort(begin, end):
            if begin == end:
                return
            pNode = partition(begin, end)
            quickSort(begin, pNode)
            quickSort(pNode.next, end)

        quickSort(head, None)
        return head