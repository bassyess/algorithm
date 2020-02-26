'''
编写一种有效的方法来检查数字是否为3的倍数
思路1：
如果数字中的数字总和为3的倍数，则数字是3的倍数
注意大数问题。
思路2：
对于23（000...10111）
1）获取所在奇数位置的计数（对于23，则为3）
2）获取偶数位置的所有计数（对于23，则为1）
3）如果上述两个计数的差是3的倍数，则数字也是3的倍数
'''
def checkNumber(num):
    if num<0:
        num = abs(num)
    if num==0:
        return True
    number = str(num)
    res = 0
    for n in number:
        res += int(n)
    if res%3 == 0:
        return True
    else:
        return False

def checkNumber2(num):
    if num<0:
        num = -num
    if num==0:
        return True
    if num==1:
        return False
    odd_count = 0
    even_count = 0
    while (num):
        if num&1:
            odd_count += 1
        if num&2:
            even_count += 1
        num = num >> 2
    return checkNumber2(abs(odd_count-even_count))

if __name__ == '__main__':
    print(checkNumber2(-21))