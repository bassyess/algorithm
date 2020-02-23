'''
5.最长回文序列
动态规划步骤：
1）定义状态，2）状态转移方程，3）初始值，4）考虑输出，5）状态压缩
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s)<=1:
            return s
        n = len(s)
        dp = [[0]*n for _ in range(n)]
        maxLen, left, right = 0, 0, 0
        for i in range(n-1,-1,-1):
            dp[i][i] = 1
            for j in range(i+1, n):
                dp[i][j] = (s[i]==s[j]) and (j-i<2 or dp[i+1][j-1])
                if dp[i][j] and maxLen<j-i+1:
                    maxLen = j-i+1
                    left, right = i, j
        return s[left:right+1]