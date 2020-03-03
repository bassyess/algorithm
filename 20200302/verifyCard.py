def isHu(nums):
    if not nums:
        return True
    n = len(nums)
    count0 =  nums.count(nums[0])
    # 没出现过雀头，且第一个数字出现的次数 >= 2,去掉雀头剩下的能不能和牌
    if n%3!=0 and count0>=2 and isHu(nums[2:])==True:
        return True
    # 如果第一个数字出现次数 >= 3，去掉这个刻子后看剩下的能和牌
    if count0>=3 and isHu(nums[3:])==True:
        return True
    # 如果存在顺子，移除顺子后剩下的能和牌
    if nums[0]+1 in nums and nums[0]+2 in nums:
        last_nums = nums.copy()
        last_nums.remove(nums[0])
        last_nums.remove(nums[0]+1)
        last_nums.remove(nums[0]+2)
        if isHu(last_nums)==True:
            return True
    # 以上条件都不满足，则不能和牌
    return False

def verifyCard(nums):
    d = {}
    for i in nums:
        d[i] = d.get(i, 0)+1
    # 卡组中还剩的牌的类型
    card_list = set(range(1, 10)) - {i for i, v in d.items() if v==4}
    res = []
    for i in card_list:
        if isHu(sorted(nums+[i])):
            res.append(i)
    res = ' '.join(str(x) for x in sorted(res)) if res else '0'
    print(res)

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    verifyCard(nums)