'''
52. N皇后
思路：回溯，主对角行号-列号=常熟，副对角行号+列号=常熟
'''


class Solution:
    def totalNQueens(self, n):
        if n == 0:
            return 0
        stack = []
        self.count = 0
        col, master, slave = set(), set(), set()
        self.helper(0, n, col, master, slave, stack)
        return self.count

    def helper(self, row, n, col, master, slave, stack):
        if row == n:
            self.count += 1
            return
        for i in range(n):
            if i not in col and row + i not in slave and row - i not in master:
                stack.append(i)
                col.add(i)
                master.add(row - i)
                slave.add(row + i)
                self.helper(row + 1, n, col, master, slave, stack)
                slave.remove(row + i)
                master.remove(row - i)
                col.remove(i)
                stack.pop()

