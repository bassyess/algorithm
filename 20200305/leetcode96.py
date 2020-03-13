'''
96. 不同的二叉搜索树
思路：遍历每一个数字i，将该数字作为根节点，则二叉排序树的个数
G(n)=f(1)+f(2)+...+f(n)，其中1,...,i-1为左子树，i+1,...,n为右子树
则f(i)=G(i-1)+G(n-i)
综合得G(n)=G(0)xG(n-1)+G(1)xG(n-2)+...+G(n-1)xG(0)
'''
def numTrees(self, n: int) -> int:
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n + 1):
        for j in range(1, i + 1):
            dp[i] += dp[j - 1] * dp[i - j]
    return dp[n]