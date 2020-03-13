'''
209. 长度最小的子数组
思路1：滑动窗口
'''


def minSubArrayLen(self, s: int, nums: List[int]) -> int:
    if not nums:
        return 0
    curSum, res = 0, float("inf")
    left, right = 0, 0
    while right < len(nums):
        curSum += nums[right]
        while curSum >= s:
            res = min(res, right - left + 1)
            curSum -= nums[left]
            left += 1
        right += 1
    return res if res != float("inf") else 0
