# 滑动窗口， 超时，完成度40%
# N, L = map(int, input().strip().split())
# left, right, Lsum = 1, 1, 0
# res = []
# mid = N//(L+1)
# minLen = float("inf")
# while left<=mid:
#     if Lsum<N:
#         Lsum += right
#         right += 1
#     elif Lsum>N:
#         Lsum -= left
#         left += 1
#     else:
#         arr = list(str(x) for x in range(left, right))
#         if len(arr)<minLen:
#             minLen = len(arr)
#             res = arr
#         Lsum -= left
#         left += 1
# print(" ".join(res))
# 利用等差数列的性质求解
N, L = map(int, input().strip().split())
flag = False
for i in range(L, 101):
    if (2*N+i-i*i)%(2*i)==0:
        flag = True
        start = (2*N+i-i*i)//(2*i)
        if start<0:
            print("No")
            exit()
        ans = [str(x) for x in range(start, start+i)]
        print(" ".join(ans))
        break
if flag==False:
    print("No")