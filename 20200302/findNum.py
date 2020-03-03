'''
思路：找到第一个比左边界大d的数，可选次数为二者中间任意取两个的可能排列
'''
def findNum(n, d, arr):
    res = 0
    left, right = 0, 2
    while left<n-2:
        while right<n and arr[right]-arr[left]<=d:
            right += 1
        if right-left-1>=2:
            num = right - left - 1
            res += num*(num-1)//2
        left += 1
    return res

if __name__ == '__main__':
    line1 = input().split(' ')
    n, d = map(int, line1)
    arr = list(map(int, input().split(' ')))
    count = findNum(n, d, arr)
    print(int(count % 99997867))