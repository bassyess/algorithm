'''
222. 完全二叉树的节点个数
'''
# 对于常规的二叉树，可以利用递归求解
def countNodes(self, root: TreeNode) -> int:
    if not root:
        return 0
    left = self.countNodes(root.left)
    right = self.countNodes(root.right)

    return left + right + 1
# 上述做法没有考虑完全二叉树的特点，满二叉树节点数为2^h-1
# 左右子树层数相等，即为完全二叉树
def countNodesII(self, root: TreeNode) -> int:
    if not root:
        return 0
    hleft = 0
    lnode = root
    hright = 0
    rnode = root
    while lnode:
        lnode = lnode.left
        hleft += 1
    while rnode:
        rnode = rnode.right
        hright += 1
    if hleft == hright:
        return pow(2, hleft) - 1
    return self.countNodes(root.left) + self.countNodes(root.right) + 1