# 划分策略，适用于链表
def partition(nums, left, right):
    if left == right:
        return left
    pivot = left
    slow, fast = left, left+1
    while fast<=right:
        if nums[fast]<nums[pivot]:
            slow += 1
            nums[slow], nums[fast] = nums[fast], nums[slow]
        fast += 1
    nums[pivot], nums[slow] = nums[slow], nums[pivot]
    return slow

# 递归方法
def quickSort(nums, left, right):
    if left<=right:
        midIndex = partition(nums, left, right)
        quickSort(nums, left, midIndex-1)
        quickSort(nums, midIndex+1, right)
    return nums

# 双指针划分
def partition2(nums, left, right):
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
# 非递归方式
# 利用栈的思想将需要继续排序的首尾下表存入栈中，不断弹栈进行分区操作
def quickSort2(nums):
    if len(nums)<=1:
        return nums
    stack = []
    left, right = 0, len(nums)-1
    stack.append(left)
    stack.append(right)
    while stack:
        r = stack.pop()
        l = stack.pop()
        midIndex = partition2(nums, l, r)
        if l<midIndex:
            stack.append(l)
            stack.append(midIndex-1)
        if r>midIndex:
            stack.append(midIndex+1)
            stack.append(r)
    return nums

if __name__ == '__main__':
    nums = [2,5,4,3,1]
    print(quickSort(nums, 0, len(nums)-1))
    # print(quickSort2(nums))