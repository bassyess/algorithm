'''
56. 数组中数字出现的次数
思路：任何数和本身异或为0，将这两个不同的数分为不同的两组。
分组依据：所有数异或一定不为0，也就是至少有一位为1，将该位为1的划分一组，为0的划分另一组。
'''
class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        res = 0
        a, b = 0, 0
        for num in nums:
            res ^= num
        bit = 1
        while res & bit == 0:
            bit = bit << 1
        for num in nums:
            if num&bit==0:
                a ^= num
            else:
                b ^= num
        return [a,b]