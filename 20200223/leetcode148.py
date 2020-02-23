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

# 快排实现