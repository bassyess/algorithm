'''
46. 全排列
思路：回溯
'''


def permute(nums):
    if len(nums) <= 1:
        return [nums]
    res, stack = [], []
    count = 0
    size = len(nums)
    used = [False]*size
    def backtrack(nums, size, count, used, stack, res):
        if count==size:
            res.append(stack[:])
            return
        for i in range(size):
            if not used[i]:
                used[i] = True
                stack.append(nums[i])
                backtrack(nums, size, count+1, used, stack, res)
                used[i] = False
                stack.pop()

    backtrack(nums, size, count, used, stack, res)
    return res

if __name__ == '__main__':
    nums = [1, 2, 3]
    print(permute(nums))