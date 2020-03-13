'''
计数排序
'''
def countingSort(nums):
    bucket = [0]*(max(nums)+1)
    for num in nums:
        bucket[num] += 1
    i = 0
    for j in range(len(bucket)):
        while bucket[j]>0:
            nums[i] = j
            bucket[j] -= 1
            i += 1
    return nums