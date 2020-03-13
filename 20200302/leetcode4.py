'''
4. 寻找两个有序数组的中位数
思路1：合并有序队列，遍历第len/2+1个元素即中位数。由于两队列之和是偶数时，
中位数为数组中间左右两数之和就平均，故需要一个变量保存前一次遍历时的值。
思路2：中位数将数组分为左右两个子序列，找两个数组中位数的两个边界值
'''

def findMedianSortedArrays(nums1, nums2):
    l1 = len(nums1)
    l2 = len(nums2)
    l = l1 + l2
    pre, cur = -1, -1
    p1, p2 = 0, 0
    for i in range(l // 2 + 1):
        pre = cur
        if p1 < l1 and (p2 >= l2 or nums1[p1] < nums2[p2]):
            cur = nums1[p1]
            p1 += 1
        else:
            cur = nums2[p2]
            p2 += 1
    if l % 2 == 0:
        return (pre + cur) / 2.0
    else:
        return cur

def findMedianSortedArraysII(nums1, nums2):
    if len(nums1)>len(nums2):
        nums1, nums2 = nums2, nums1
    l1, l2 = len(nums1), len(nums2)
    mid = (l1+l2+1)//2
    left, right = 0, l1
    while left<right:
        mid1 = left+(right-left)//2
        mid2 = mid - mid1
        if nums1[mid1]<nums2[mid2-1]:
            left = mid1+1
        else:
            right = mid1
    mid1 = left
    mid2 = mid - mid1
    if mid1 == 0:
        max_out_left = nums2[mid2-1]
    elif mid2 == 0:
        max_out_left = nums1[mid1-1]
    else:
        max_out_left = max(nums1[mid1-1], nums2[mid2-1])
    if (l1+l2)%2 == 1:
        return max_out_left
    if mid1 == l1:
        min_out_right = nums2[mid2]
    elif mid2 == l2:
        min_out_right = nums1[mid1]
    else:
        min_out_right = min(nums1[mid1], nums2[mid2])
    return (max_out_left+min_out_right)/2.0

if __name__ == '__main__':
    nums1 = [1, 3]
    nums2 = [2]
    print(findMedianSortedArrays(nums1, nums2))