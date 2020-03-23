'''
美团笔试 3.20
数组长度为n，从中删除一个数字，求最长上升子数组的长度，a[i+1]>a[i]
例子：
n
数组输入
5
1 2 5 3 4
输出
4
'''
n = int(input().strip())
nums = list(map(int, input().strip().split()))
def longestOfLST(nums):
    if not nums:
        return 0
    dp = [1]*(len(nums))
    for i in range(len(nums)):
        for j in range(i):
            if nums[i]>nums[j]:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)
maxLen = 0
for i in range(len(nums)):
    tmp = longestOfLST(nums[:i]+nums[i+1:])
    if tmp>maxLen:
        maxLen = tmp
print(maxLen)

