'''
658. 找到k个最接近的元素
思路：将其转化为找最左边界，然后二分查找
'''


def findClosestElements(arr, k, x):
    if x < arr[0]:
        return arr[:k]
    n = len(arr)
    if x > arr[-1]:
        return arr[n - k:]
    left, right = 0, n - k
    while left < right:
        mid = (left + right) // 2
        if x - arr[mid] > arr[mid + k] - x:
            left = mid + 1
        else:
            right = mid
    return arr[left:left + k]