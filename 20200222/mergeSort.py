'''
归并排序
思路：将数组看成两个有序的子数列
'''
def merge(left, right):
    res = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res += left[i:] if i < len(left) else right[j:]
    return res

# 递归版本
def mergeSort(nums):
    if len(nums)<=1:
        return nums

    mid = len(nums)//2
    left = mergeSort(nums[:mid])
    right = mergeSort(nums[mid:])
    return merge(left, right)

# 非递归版本
def mergeSort2(nums):
    i = 1  # i是步长
    while i<len(nums):
        left = 0
        while left<len(nums):
            mid = left+i
            right = min(left+2*i, len(nums))
            if mid<right:
                nums[left:right]=merge(nums[left:mid], nums[mid:right])
            left += 2*i
        i *= 2
    return nums

if __name__ == '__main__':
    print(mergeSort2([2,5,4,3,1]))