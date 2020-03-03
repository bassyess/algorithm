'''
4. 寻找两个有序数组的中位数
'''


def findMedianSortedArrays(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    m, n = len(nums1), len(nums2)
    left, right, midLen = 0, m, (m + n + 1) // 2
    mid1 = (left + right) // 2
    mid2 = midLen - mid1
    while left < right:
        if mid1 < m and nums2[mid2-1] > nums1[mid1]:
            left = mid1 + 1
        else:
            right = mid1
        mid1 = (left + right) // 2
        mid2 = midLen - mid1
    if mid1 == 0:
        max_out_left = nums2[mid2-1]
    elif mid2 == 0:
        max_out_left = nums1[mid1-1]
    else:
        max_out_left = max(nums1[mid1-1], nums2[mid2-1])
    if (m + n) % 2 == 1:
        return max_out_left
    if mid1 == m:
        min_out_right = nums2[mid2]
    elif mid2 == n:
        min_out_right = nums1[mid1]
    else:
        min_out_right = min(nums1[mid1], nums2[mid2])
    return (max_out_left + min_out_right) / 2.0

if __name__ == '__main__':
    nums1 = [1, 3]
    nums2 = [2]
    print(findMedianSortedArrays(nums1, nums2))