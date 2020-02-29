'''
37. 解数独
'''
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = [set(range(1, 10)) for _ in range(9)]
        col = [set(range(1, 10)) for _ in range(9)]
        block = [set(range(1, 10)) for _ in range(9)]

        empty = []
        for i in range(9):
            for j in range(9):
                if board[i][j]!='.':
                    val = int(board[i][j])
                    row[i].remove(val)
                    col[j].remove(val)
                    block[(i//3)*3+j//3].remove(val)
                else:
                    empty.append((i,j))
        def helper(count):
            if count==len(empty):
                return True
            i, j = empty[count]
            b = (i//3)*3+j//3
            for val in row[i] & col[j] & block[b]:
                row[i].remove(val)
                col[j].remove(val)
                block[b].remove(val)
                board[i][j] = str(val)
                if helper(count+1):
                    return True
                block[b].add(val)
                col[j].add(val)
                row[i].add(val)
            return False
        helper(0)