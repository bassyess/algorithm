'''
142. 环形链表
思路：先检测链路中是否有环，有环则快慢指针相遇；
然后将其中一个指针放回head，两指针第二次相遇即环的入口
'''


def detectCycle(self, head: ListNode) -> ListNode:
    if not head or not head.next:
        return None
    slow, fast = head, head
    while True:
        if not (fast and fast.next):
            return None
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            break
    slow = head
    while fast != slow:
        fast = fast.next
        slow = slow.next
    return slow