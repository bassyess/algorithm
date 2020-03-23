'''
美团笔试3.12
给出一个序列包含n个正整数的序列A，然后给出一个正整数x，你可以对序列进行
任意次操作的，每次操作你可以选择序列中的一个数字，让其与x做按位或运算。你的目的是
让这个序列中的众数出现的次数最多。
输入第一行仅包含两个正整数n和x，表示给出的序列的长度和给定的正整数。
(1<=n<=100000, 1<=x<=1000)
接下来一行有n个正整数，及这个序列，中间用空格隔开。(1<=a_i<=1000)
输出仅包含一个正整数，表示众数最多出现的次数
'''
n, x = map(int, input().strip().split())
nums = list(map(int, input().strip().split()))
dic = {}
for i in range(len(nums)):
    dic[nums[i]] = dic.get(nums[i], 0)+1
    xi = x|nums[i]
    if nums[i]!=xi:
        dic[xi] = dic.get(xi, 0)+1
print(max(dic.values()))