'''
给定N个元素，找到所需的最小交换数，以便最大元素在开头，
最小元素在最后，但仅允许相邻元素交换。
'''
def minSwaps(arr):
    n = len(arr)
    maxx, minn, l, r = -1, arr[0], 0, 0
    for i in range(n):
        if arr[i]>maxx:
            maxx = arr[i]
            l = i
        if arr[i]<=minn:
            minn = arr[i]
            r = i
    if r<l:
        print(l+(n-r-2))
    else:
        print(l+(n-r-1))
