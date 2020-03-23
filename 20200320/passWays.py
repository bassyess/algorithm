'''
美团笔试 3.12

两行长度均为 n 字符串，仅包含字符'X`(代表障碍物)和'.'(可以通行)，
初始在左上角(1, 1)，想到右下角(2, n)去，求方案数，如果不能到(2, n) 输出-1。
数据范围：1<= n <= 50。
'''
# n = int(input().strip())
# def helper(nums, i, j, stack, res):
#     if (i, j) == (1, n-1) and nums[i][j]=='.':
#         res.append(stack[:])
#         return
#     if nums[i][j]=='.':
#         stack.append((i, j))
#         if i<=0 and nums[i+1][j]=='.':
#             helper(nums, i+1, j, stack, res)
#         if j<=n-2 and nums[i][j+1]=='.':
#             helper(nums, i, j+1, stack, res)
#         stack.pop()
# if n>=1 and n<=50:
#     data = []
#     for i in range(2):
#         s = list(map(str, input().strip()))
#         data.append(s)
#     res = []
#     helper(data, 0, 0, [], res)
#     print(len(res))
# else:
#     print(-1)

# 动规
n = int(input().strip())
if n>=1 and n<=50:
    data = []
    for i in range(2):
        s = list(map(str, input().strip()))
        data.append(s)
    dp = [[0]*n for _ in range(2)]
    if data[0][0] == '.':
        dp[0][0] = 1
    else:
        print(-1)
    for i in range(1, n):
        if data[0][i] == '.' and dp[0][i-1]==1:
            dp[0][i] = 1
        else:
            dp[0][i] = 0
    dp[1][0] = 1 if data[1][0]=='.' else 0
    for i in range(1, n):
        dp[1][i] = dp[1][i-1]+dp[0][i]
    print(dp[-1][-1])
else:
    print(-1)