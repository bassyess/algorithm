'''
104. 二叉树的最大深度
思路：递归或迭代
'''


def maxDepth(root):
    if not root:
        return 0
    left = maxDepth(root.left)
    right = maxDepth(root.right)

    return max(left + 1, right + 1)+1

# 迭代
def maxDepthII(root):
    if not root:
        return 0
    stack = [(root, 1)]
    depth = 0
    while stack:
        node, curDepth = stack.pop()
        if node:
            depth = max(depth, curDepth)
            stack.append((node.left, curDepth + 1))
            stack.append((node.right, curDepth + 1))
    return depth