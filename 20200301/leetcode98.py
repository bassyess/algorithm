'''
98. 验证二叉搜索树
思路：中序遍历，递增序列
'''
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack, inorder = [], float("-inf")
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val<=inorder:
                return False
            inorder = root.val
            root = root.right
        return True