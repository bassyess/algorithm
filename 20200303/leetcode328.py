'''
328. 奇偶链表
'''


def oddEvenList(self, head: ListNode) -> ListNode:
    if not head:
        return
    odd, even, evenHead = head, head.next, head.next
    while even and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next
    odd.next = evenHead
    return head