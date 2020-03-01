'''
56-2:数字中出现的次数2
思路：三进制，将数字的二进制每一位进行求和，若该位不是3的倍数，则这个数字在该位置为1.
'''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(32):
            bit = 1<<i
            cnt = 0
            for num in nums:
                if num&bit!=0:
                    cnt += 1
            if cnt%3!=0:
                res |= bit
        return res