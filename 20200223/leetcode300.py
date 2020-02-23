'''
300.最长上升序列
'''
# 动态规划
def lengthOfLIS(nums):
    if not nums or len(nums) <= 1:
        return nums
    n = len(nums)
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

# 进阶：将算法的时间复杂度降低为O(nlogn)
# 贪心+二分查找， 序列长度正确，但序列元素不对
def lengthOfLIS2(nums):
    n = len(nums)
    if n < 2:
        return n
    res = [nums[0]]
    for num in nums[1:]:
        if num > res[-1]:
            res.append(num)
            continue
        left, right = 0, len(res) - 1
        while left < right:
            mid = left + (right - left) // 2
            if res[mid] < num:
                left = mid + 1
            else:
                right = mid
        res[left] = num
    return len(res)

if __name__ == '__main__':
    nums = [10,9,2,5,3,7,101,1]
    print(lengthOfLIS2(nums))