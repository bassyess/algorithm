'''
235. 二叉搜索树的最近公共祖先
思路：给定的两个数小于根节点，则一定在左子树中
给定的两个数大于根节点，则一定在右子树中
给地的两个数一个大于根节点，一个小于根节点，则公共祖先一定是根节点
'''
# 递归
def lowestCommonAncestor(root, p, q):
    if not root:
        return
    if p.val<root.val and q.val<root.val:
        return lowestCommonAncestor(root.left, p, q)
    if p.val>root.val and q.val>root.val:
        return lowestCommonAncestor(root.right, p, q)
    else:
        return root
# 迭代
def lowestCommonAncestorII(root, p, q):
    p_val = p.val
    q_val = q.val
    node = root
    while node:
        parent_val = node.val
        if p_val > parent_val and q_val > parent_val:
            node = node.right
        elif p_val < parent_val and q_val < parent_val:
            node = node.left
        else:
            return node

'''
236. 二叉树的最近公共祖先
思路：给定标志位判断p,q节点是在左子树还是右子树，
找到对应的节点后往上抛出
'''
# 递归
def lowestCommonAncestorIII(root, p, q):
    if root==None or root==p or root==q:
        return root
    left = lowestCommonAncestorIII(root.left, p, q)
    right = lowestCommonAncestorIII(root.right, p, q)
    if left==None and right==None:
        return None
    elif left!=None and right!=None:
        return root
    else:
        return left if right==None else right

# 迭代
def lowestCommonAncestorIV(root, p, q):
    stack = [root]
    while len(stack)>0:
        node = stack.pop()
        