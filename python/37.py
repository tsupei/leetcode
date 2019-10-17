import time
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # for i in range(9):
        #     print(board[i])
        # print("\n")
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for k in range(1,10):
                        if str(k) in board[i]:
                            continue
                        if str(k) in [board[t][j] for t in range(9)]:
                            continue
                        row_offset = (i//3)*3
                        col_offset = (j//3)*3
                        if str(k) in board[row_offset][col_offset:col_offset+3]:
                            continue
                        if str(k) in board[row_offset+1][col_offset:col_offset+3]:
                            continue
                        if str(k) in board[row_offset+2][col_offset:col_offset+3]:
                            continue
                        board[i][j] = str(k)
                        if self.solveSudoku(board):
                            return True
                    board[i][j] = '.'
                    return False
        return True

if __name__ == "__main__":
    sol = Solution()
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    b = sol.solveSudoku(board)
    print(board)