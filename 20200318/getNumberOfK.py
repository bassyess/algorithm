def GetNumberOfK(data, k):
    # write code here
    if not data:
        return 0
    count = 0
    first = getFirstNumber(data, k, 0, len(data) - 1)
    last = getLastNumber(data, k, 0, len(data) - 1)
    print(last, first)
    if first > -1 and last > -1:
        if last == first:
            count = 0
        else:
            count = last - first + 1
    return count


def getFirstNumber(nums, k, start, end):
    if start > end:
        return -1
    while start < end:
        mid = start + (end - start) // 2
        if nums[mid] == k:
            if mid > 0 and nums[mid - 1] == k:
                end = mid - 1
            else:
                return mid
        elif nums[mid] > k:
            end = mid - 1
        else:
            start = mid + 1
    return start


def getLastNumber(nums, k, start, end):
    if start > end:
        return -1
    while start < end:
        mid = start + (end - start) // 2
        if nums[mid] == k:
            if mid < len(nums) - 1 and nums[mid + 1] == k:
                start = mid + 1
            else:
                return mid
        elif nums[mid] > k:
            end = mid - 1
        else:
            start = mid + 1
    return start

if __name__ == '__main__':
    nums = [3]
    print(GetNumberOfK(nums, 3))