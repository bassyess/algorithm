def lengthOfLongestSubstring(s):
    from collections import defaultdict
    if not s:
        return 0
    if len(s)==1:
        return 1
    left, right, counter = 0, 0, 0
    maxLen = 0
    winds = defaultdict(int)
    while right<len(s):
        if winds[s[right]]>0:
            counter += 1
        winds[s[right]] += 1
        right += 1
        while counter>0:
            if winds[s[left]]>1:
                counter -= 1
            winds[s[left]] -= 1
            left += 1
        maxLen = max(maxLen, right-left)
    return maxLen

def preOrder(node):
    if not node:
        return None
    print(node.val)
    preOrder(node.left)
    preOrder(node.right)
def preOrderII(node):
    stack = [node]
    while stack:
        print(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
        node = stack.pop()
def inOrder(node):
    if not node:
        return None
    inOrder(node.left)
    print(node.val)
    inOrder(node.right)
def InOrderII(node):
    stack = [node]
    while node or len(stack)>0:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        print(node.val)
        node = node.right
def postOrder(node):
    if not node:
        return None
    postOrder(node.left)
    postOrder(node.right)
    print(node.val)
def postOrderII(node):
    stack = [node]
    stack2 = []
    while stack:
        node = stack.pop()
        stack2.append(node)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    while len(stack2)>0:
        print(stack2.pop().val)
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

def quickSort(nums, left, right):
    def partition(nums, left, right):
        if left==right:
            return left
        pivot = left
        slow, fast = left, left+1
        while fast<=right:
            if nums[fast]<nums[pivot]:
                slow += 1
                nums[fast], nums[slow] = nums[slow], nums[fast]
            fast += 1
        nums[pivot], nums[slow] = nums[slow], nums[pivot]
        return slow
    if left<=right:
        midIndex = partition(nums, left, right)
        quickSort(nums, left, midIndex-1)
        quickSort(nums, midIndex+1, right)
def quickSortII(nums):
    def partition(nums, left, right):
        mid = nums[left]
        while left<right:
            while left<right and nums[right]>mid:
                right -= 1
            nums[left] = nums[right]
            while left<right and nums[left]<=mid:
                left += 1
            nums[right] = nums[left]
        nums[left] = mid
        return left

    if len(nums)<=1:
        return nums
    stack = []
    left, right = 0, len(nums)-1
    stack.append(left)
    stack.append(right)
    while stack:
        r = stack.pop()
        l = stack.pop()
        midIndex = partition(nums, l, r)
        if l<midIndex:
            stack.append(l)
            stack.append(midIndex-1)
        if r>midIndex:
            stack.append(midIndex+1)
            stack.append(r)
    return nums
def merge(left, right):
    res = []
    i = j = 0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res = res + left[i:] + right[j:]
    return res
def mergeSort(nums):
    if len(nums)<=1:
        return nums
    mid = len(nums)//2
    left = mergeSort(nums[:mid])
    right = mergeSort(nums[mid:])
    return merge(left, right)
def mergeSortII(nums):
    i = 1
    while i<len(nums):
        left = 0
        while left<len(nums):
            mid = left + i
            right = min(left+2*i, len(nums))
            if mid<right:
                nums[left:right] = merge(nums[left:mid],nums[mid:right])
            left += 2*i
        i *= 2
    return nums

def heapSort(nums):
    def adjustHeap(nums, i, size):
        lchild = 2*i+1
        rchild = 2*i+2
        largest = i
        if lchild<size and nums[lchild]>nums[largest]:
            largest = lchild
        if rchild<size and nums[rchild]>nums[largest]:
            largest = rchild
        if largest != i:
            nums[largest], nums[i] = nums[i], nums[largest]
            adjustHeap(nums, largest, size)

    def buildHeap(nums, size):
        for i in range(len(nums)//2)[::-1]:
            adjustHeap(nums, i, size)
    size = len(nums)
    buildHeap(nums, size)
    for i in range(len(nums))[::-1]:
        nums[0], nums[i] = nums[i], nums[0]
        adjustHeap(nums, 0, i)

def countSort(nums):
    bucket = [0]*max((nums)+1)
    for num in nums:
        bucket[num] += 1
    i = 0
    for j in range(len(bucket)):
        while bucket[j]>0:
            nums[i] = j
            bucket[j] -= 1
            i += 1
    return nums