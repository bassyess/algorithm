'''
77. 组合
思想：回溯
'''

def combine(self, n: int, k: int) -> List[List[int]]:
    stack, res = [], []
    def backtrack(n, start, k, stack, res):
        if len(stack) == k:
            res.append(stack[:])
            return
        for i in range(start, n + 1):
            stack.append(i)
            backtrack(n, i + 1, k, stack, res)
            stack.pop()
    backtrack(n, 1, k, stack, res)
    return res