import time
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # row
        for i in range(9):
            check = [0] * 10
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j])
                    if check[num] == 1:
                        return False
                    check[num] = 1
        # col
        for j in range(9):
            check = [0] * 10
            for i in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j])      
                    if check[num] == 1:
                        return False
                    check[num] = 1

        # block
        for i in range(3):
            for j in range(3):
                check = [0] * 10
                for m in range(3):
                    for n in range(3):
                        if board[i*3+m][j*3+n] != '.':
                            num = int(board[i*3+m][j*3+n])
                            if check[num] == 1:
                                return False
                            check[num] = 1
        return True


if __name__ == "__main__":
    sol = Solution()
    board = [[".","8","7","6","5","4","3","2","1"],["2",".",".",".",".",".",".",".","."],["3",".",".",".",".",".",".",".","."],["4",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".",".","."],["6",".",".",".",".",".",".",".","."],["7",".",".",".",".",".",".",".","."],["8",".",".",".",".",".",".",".","."],["9",".",".",".",".",".",".",".","."]]
    b = sol.isValidSudoku(board)
    print(b)