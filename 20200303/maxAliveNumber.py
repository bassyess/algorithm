'''
面试题16.10 生存人数
思路：统计每年的出生人数和死亡人数，然后相减求每年的生存人数
'''
def maxAliveYear(self, birth: List[int], death: List[int]) -> int:
    birthNum, deathNum = [0] * 101, [0] * 101
    maxNum, ret = 0, -1
    for i in range(len(birth)):
        birthNum[birth[i] - 1900] += 1
        deathNum[death[i] - 1900] += 1
    for i in range(1, len(birthNum)):
        birthNum[i] = birthNum[i] + birthNum[i - 1]
        deathNum[i] = deathNum[i] + deathNum[i - 1]
    for i in range(len(birthNum)):
        if i == 0 and maxNum < birthNum[i]:
            maxNum = birthNum[i]
            ret = 0
        if i != 0 and maxNum < birthNum[i] - deathNum[i - 1]:
            maxNum = birthNum[i] - deathNum[i - 1]
            ret = i
    return ret + 1900