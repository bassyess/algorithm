'''
53. 最大子序列和
思路：对数组进行遍历，当前最大连续子序列和为nsum，
若nsum>0，则对序列结果有增益，nsum加上该数字
若nsum<=0，则nsum对结果无增益效果，将nsum直接更新为当前遍历值
遍历过程比较nsum和res的最大值
'''


def maxSubArray(self, nums: List[int]) -> int:
    res = nums[0]
    nsum = 0
    for num in nums:
        if nsum > 0:
            nsum += num
        else:
            nsum = num
        res = max(res, nsum)
    return res