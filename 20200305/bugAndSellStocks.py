# 买卖股票问题整理
'''
1. 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
如果你最多只允许完成一笔交易（即买入和卖出一支股票），求获得的最大利润。
思路1：dp[i][j]表示第i天用户持股为j所获最大利润。
j只有两个值：0表示不持股，1表示持股。
则dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
dp[i][1] = max(dp[i-1][1], -prices[i])，因为题目只允许一次交易，因此不能加上dp[i-1][0]
初始值：第0天不持股，dp[0][0]=0；第0天持股，dp[0][1]=-prices[0]
'''
def maxProfit(prices):
    if len(prices)<2:
        return 0
    n = len(prices)
    dp = [[0]*n for _ in range(2)]
    dp[0][0] = 0
    dp[0][1] = -prices[0]
    for i in range(1, n):
        dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
        dp[i][1] = max(dp[i-1][1], -prices[i])
    return dp[-1][0]
# 考虑状态压缩，dp[i]仅仅依赖于dp[i-1]
def maxProfit2(prices):
    n = len(prices)
    if n<2:
        return 0
    dp = [0]*2
    dp[0] = 0
    dp[1] = -prices[0]
    for i in range(1, n):
        dp[0] = max(dp[0], dp[1]+prices[i])
        dp[1] = max(dp[1], -prices[i])
    return dp[0]

'''
2.可以尽可能地完成更多的交易（多次买卖一支股票），
但不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）
思路：dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i])
dp[0][0] = 0, dp[0][1] = -prices[0]
'''
def maxProfitII(prices):
    n = len(prices)
    if n<2:
        return 0
    dp = [[0]*2 for _ in range(n)]
    dp[0][0] = 0
    dp[0][1] = -prices[0]
    for i in range(1, n):
        dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
        dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i])
    return dp[-1][0]
# 考虑状态压缩 dp[i]也仅仅依赖dp[i-1]

'''
3. 最多可以完成两笔交易。
注：必须在再次购买前出售掉之前的股票
思路：重新定义状态方程
dp[i][0]表示未交易
dp[i][1]表示第一次买入一支股票
dp[i][2]表示第一次卖出一支股票
dp[i][3]表示第二次买入一支股票
dp[i][4]表示第二次卖出一支股票
状态转移方程见代码
初始化：第0天初始化为前两个状态，而状态3（第二次
持股）只能赋值为一个不可能的数。
'''
def maxProfitIII(prices):
    n = len(prices)
    if n<2:
        return 0
    dp = [[0]*5 for _ in range(n)]
    dp[0][1] = -prices[0]
    for i in range(n):
        dp[i][3] = float("-inf")
    for i in range(1, n):
        dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i])
        dp[i][2] = max(dp[i-1][2], dp[i-1][1]+prices[i])
        dp[i][3] = max(dp[i-1][3], dp[i-1][2]-prices[i])
        dp[i][4] = max(dp[i-1][4], dp[i-1][3]+prices[i])
    # 最大值只发生在不持股的时候
    return max(0, dp[-1][2], dp[-1][4])
# 状态压缩，dp[i]仅仅依赖于dp[i-1]

'''
4. 最多可以完成 k 笔交易
注：必须在再次购买前出售掉之前的股票
'''

'''
5. 在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:
1) 必须在再次购买前出售掉之前的股票;
2) 卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)
思路：增加一个状态，j取三个值：
0表示不持股，1表示持股，2表示冷冻期
状态转移方程：
dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
dp[i][1] = max(dp[i-1][1], dp[i-1][2]-prices[i])
dp[i][2] = dp[i-1][0]
'''
def maxProfitV(prices):
    n = len(prices)
    if n<2:
        return 0
    dp = [[0]*3 for _ in range(n)]
    dp[0][1] = -prices[0]
    for i in range(1, n):
        dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
        dp[i][1] = max(dp[i-1][1], dp[i-1][2]-prices[i])
        dp[i][2] = dp[i-1][0]
    return max(dp[-1][0], dp[-1][2])
# 考虑状态压缩，dp[i]仅仅只依赖于dp[i-1]

'''
6. 你可以无限次地完成交易，但是你每次交易都需要付手续费fee。
如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。
思路：规定手续费在买入股票时扣除
状态转移方程：
dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i]-fee)
'''
def maxProfitVI(prices, fee):
    n = len(prices)
    if n<2:
        return 0
    dp = [[0]*2 for _ in range(n)]
    dp[0][1] = -prices[0]-fee
    for i in range(1, n):
        dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
        dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i]-fee)
    return dp[-1][0]