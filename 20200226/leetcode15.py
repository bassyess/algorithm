'''
15. 三数之和
思路：难点在于如何去除重复解，排序+双指针
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        n = len(nums)
        nums.sort()
        res = []
        for i in range(n):
            if nums[i]>0:
                return res
            if i>0 and nums[i]==nums[i-1]:
                continue
            left, right = i+1, n-1
            while left<right:
                if nums[i]+nums[left]+nums[right]==0:
                    res.append([nums[i],nums[left],nums[right]])
                    while left<right and nums[left+1]==nums[left]:
                        left += 1
                    while left<right and nums[right-1]==nums[right]:
                        right -= 1
                    left += 1
                    right -= 1
                elif nums[i]+nums[left]+nums[right]<0:
                    left += 1
                else:
                    right -= 1
        return res