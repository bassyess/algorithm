'''
221. 最大正方形
思路：设dp[i][j]表示该处由1组成的最大正方形的边长
则dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
同时再引入一个变量记录当前出现的最大边长
'''


def maximalSquare(self, matrix: List[List[str]]) -> int:
    if not matrix or len(matrix) < 1 or len(matrix[0]) < 1:
        return 0
    rows, cols = len(matrix), len(matrix[0])
    maxSide = 0
    dp = [[0] * (cols + 1) for _ in range(rows + 1)]
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            if matrix[i - 1][j - 1] == '1':
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                maxSide = max(maxSide, dp[i][j])
    return maxSide * maxSide

# 空间优化，在状态转移方程中，我们只利用了左侧元素和上一行的元素，不需要维护二维dp矩阵。
def maximalSquareII(self, matrix: List[List[str]]) -> int:
    if not matrix or len(matrix) < 1 or len(matrix[0]) < 1:
        return 0
    rows, cols = len(matrix), len(matrix[0])
    maxSide = 0
    dp = [0] * (cols + 1)
    prev = 0
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            temp = dp[j]
            if matrix[i - 1][j - 1] == '1':
                dp[j] = min(dp[j - 1], dp[j], prev) + 1
                maxSide = max(maxSide, dp[j])
            else:
                dp[j] = 0
            prev = temp
    return maxSide * maxSide