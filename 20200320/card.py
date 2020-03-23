'''
阿里笔试3.20
有一叠扑克牌，每张牌介于1和10之间
有四种出牌方法：
单出1张
出2张对子
出五张顺子，如12345
出三连对子，如112233
给10个数，表示1-10每种牌有几张，问最少要多少次能出完
'''
if __name__ == '__main__':
    nums = list(map(int, input().strip().split()))
    res = []
    def helper(nums, count, res):
        i = 0
        while i<10:
            if nums[i]>0:
                break
            i += 1
        if i == 10:
            res.append(count)
            return
        if i+2<10 and nums[i]>=2 and nums[i+1]>=2 and nums[i+2]>=2:
            nums[i] -= 2
            nums[i+1] -= 2
            nums[i+2] -= 2
            helper(nums, count+1, res)
            nums[i+2] += 2
            nums[i+1] += 2
            nums[i] += 2
        if i+4<10 and nums[i]>=1 and nums[i+1]>=1 and nums[i+2]>=1 and nums[i+3]>=1 and nums[i+4]>=1:
            nums[i] -= 1
            nums[i+1] -= 1
            nums[i+2] -= 1
            nums[i+3] -= 1
            nums[i+4] -= 1
            helper(nums, count+1, res)
            nums[i+4] += 1
            nums[i+3] += 1
            nums[i+2] += 1
            nums[i+1] += 1
            nums[i] += 1
        if i<10 and nums[i]>=2:
            nums[i] -= 2
            helper(nums, count+1, res)
            nums[i] += 2
        if i<10 and nums[i]>=1:
            nums[i] -= 1
            helper(nums, count+1, res)
            nums[i] += 1
    helper(nums, 0, res)
    print(min(res))

