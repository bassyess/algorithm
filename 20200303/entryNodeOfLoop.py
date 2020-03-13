'''
如果一个链表包含环，如何找到环的入口节点
'''
def entryNodeOfLoop(head):
    pFast = head
    pSlow = head
    while pFast!=None and pFast.next!=None:
        pFast = pFast.next.next
        pSlow = pSlow.next
        if pFast == pSlow:
            break
    if pFast==None or pFast.next==None:
        return None
    pFast = head
    while pFast!=pSlow:
        pFast = pFast.next
        pSlow = pSlow.next
    return pFast