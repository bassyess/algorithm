n = int(input().strip())
words = [""]*(n+1)
for i in range(1, n+1):
    words[i] = str(input().strip())
try:
    while True:
        index = list(map(int, input().strip().split()))
        l1 = len(words[index[0]])
        l2 = len(words[index[1]])
        count = 0
        for i in range(min(l1, l2)):
            if words[index[0]][i] == words[index[1]][i]:
                count += 1
            else:
                break
        print(count)
except:
    pass