'''
美团笔试 3.20
两个人从自己的牌库中抽牌，牌库长度为n，两人各抽三张求和，求两人可以取到的最大值
'''
n = int(input().strip())
a = list(map(int, input().strip().split()))
b = list(map(int, input().strip().split()))
a.sort(reverse=True)
aThreeSum = a[0]+a[1]+a[2]
b.sort(reverse=True)
bThreeSum = b[0]+b[1]+b[2]
ans = aThreeSum if aThreeSum>bThreeSum else bThreeSum
print(ans)
