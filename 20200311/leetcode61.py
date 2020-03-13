'''
61. 旋转数组
思路：先将尾部节点和头节点相连，再判断旋转后的位置进行切分
'''
def rotateRight(head, k):
    if not head or not head.next:
        return head
    old_tail = head
    n = 1
    while old_tail and old_tail.next:
        old_tail = old_tail.next
        n += 1
    old_tail.next = head
    new_tail = head
    for i in range(n - k % n - 1):
        new_tail = new_tail.next
    new_head = new_tail.next
    new_tail.next = None
    return new_head