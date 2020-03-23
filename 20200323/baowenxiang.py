import sys
n = int(input().strip())
lines = sys.stdin.readlines()
if len(lines)==1:
    temp = list(map(int, lines[0].strip().split()))
    food = temp[:n]
    capacity = temp[n:]
else:
    food = list(map(int, lines[0].strip().split()))
    capacity = list(map(int, lines[1].strip().split()))

max_food = sum(food)
max_capacity = sum(capacity)
dp = [[len(food), 0] for _ in range(max_capacity+1)]
dp[0] = [0, 0]

for k in range(1, n + 1):
    for i in range(max_capacity, 0, -1):
        count = dp[max(i - capacity[k - 1], 0)][0]
        weight = dp[max(i - capacity[k - 1], 0)][1]
        if dp[i][0] < count + 1:
            continue
        elif dp[i][0] > count + 1:
            dp[i][0] = count + 1
            dp[i][1] = weight + food[k - 1]
        else:
            dp[i][1] = max(weight + food[k - 1], dp[i][1])

min_step = 0
min_bin = n
for i in range(max_food, max_capacity + 1):
    if dp[i][0] < min_bin:
        min_bin = dp[i][0]
        min_step = dp[i][1]
    elif dp[i][0] == min_bin:
        min_step = max(dp[i][0], min_step)
min_step = max_food - min_step
# print(max_food, min_step)
print(str(min_bin) + ' ' + str(min_step))
