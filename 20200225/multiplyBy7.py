'''
乘7的有效方法
思路：将一个数n左移3位得到8n，然后将去原来的数即8n-n=7n
'''
def multiplyBy7(num):
    return (num<<3)-num

if __name__ == '__main__':
    print(multiplyBy7(6))