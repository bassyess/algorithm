'''
树的前序、中序、后序、层次
'''
# 前序:根节点->左子树->右子树
## 递归
def preOrder(node):
    if not node:
        return None
    print(node.val)
    preOrder(node.left)
    preOrder(node.right)
## 非递归
def preOrder2(node):
    stack = [node]
    while stack:
        print(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
        node = stack.pop()

# 中序遍历：左子树->根节点->右子树
## 递归
def inorder(node):
    if not node:
        return None
    inorder(node.left)
    print(node.val)
    inorder(node.right)
## 非递归
def inorder2(node):
    stack = []
    while node or len(stack)>0:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        print(node.val)
        node = node.right

# 后序遍历：左子树->右子树->根节点
## 递归
def postOrder(node):
    if not node:
        return None
    postOrder(node.left)
    postOrder(node.right)
    print(node.val)
'''
使用两个栈结构
第一个栈进栈顺序：左节点->右节点->根节点
第一个栈弹出顺序：根节点->右节点->左节点
第二个栈存储为第一个栈的每个弹出依次入栈
最后第二个栈依次出栈
'''
def postOrder2(node):
    stack = [node]
    stack2 = []
    while len(stack)>0:
        node = stack.pop()
        stack2.append(node)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    while len(stack2)>0:
        print(stack2.pop().val)

# 层次遍历
def layerOrder(node):
    if not node:
        return None
    queue = []
    queue.append(node)
    while len(queue)>0:
        node = queue.pop(0)
        print(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)