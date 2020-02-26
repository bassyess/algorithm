'''
152.乘积最大子序列
思路：保留当前值前i个的最大值和最小值
'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return
        preMax, preMin, res = nums[0], nums[0], nums[0]
        for num in nums[1:]:
            curMax = max(preMax*num, preMin*num, num)
            curMin = min(preMax*num, preMin*num, num)
            res = max(curMax, res)
            preMax = curMax
            preMin = curMin
        return res