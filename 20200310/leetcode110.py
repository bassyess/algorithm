'''
110. 平衡二叉树
思路：自顶向下，暴力求解
'''


def isBalanced(self, root: TreeNode) -> bool:
    if not root:
        return True
    if abs(self.depth(root.left) - self.depth(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(
            root.right):
        return True
    else:
        return False


def depth(self, root):
    if not root:
        return 0
    left = self.depth(root.left)
    right = self.depth(root.right)
    return max(left, right) + 1