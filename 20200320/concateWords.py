'''
阿里笔试3.20
首先定义上升字符串，s[i] >= s[i-1],比如aaa，abc是，acb不是
给n个上升字符串，选择任意个拼起来，问能拼出来的最长上升字符串长度
'''
n = int(input().strip())
words = []
dp = [0]*26
for i in range(n):
    s = str(input().strip())
    words.append(s)
words.sort()
for i in range(n):
    start = ord(words[i][0])-ord('a')
    last = ord(words[i][-1])-ord('a')
    tmp = 0
    for j in range(start+1):
        tmp = max(dp[j], tmp)
    dp[last] = max(dp[last], tmp+len(words[i]))
print(max(dp))