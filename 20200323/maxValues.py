n = int(input().strip())
values = [[0]*2 for _ in range(n+1)]
for i in range(1, n+1):
    values[i] = list(map(int, input().strip().split()))
dp = [0]*(n+1)
dp[1] = values[1][0]
for i in range(2, n+1):
    dp[i] = max(dp[i-2]+values[i][1], dp[i-1]+values[i][0])
print(dp[-1])