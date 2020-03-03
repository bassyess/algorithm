'''
725.分割链表
思路：先遍历链表获得链表长度，均匀划分每个部分的长度
'''

def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
    length = 0
    pNode = root
    while pNode:
        length += 1
        pNode = pNode.next
    sublen = length // k
    rest = length % k
    res = [None for _ in range(k)]
    pNode = root
    i = 0
    while i < k and pNode:
        res[i] = pNode
        seglen = sublen + 1 if rest > 0 else sublen
        for j in range(seglen):
            pPrev = pNode
            pNode = pNode.next
        pPrev.next = None
        i += 1
        rest -= 1
    return res