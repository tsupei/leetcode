class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        if not board[0]:
            return 
        n = len(board)
        m = len(board[0])
        for i in range(n):
            for j in range(m):
                # if 0 -> 1 set 2
                # if 1 -> 0 set 3
                cnt = 0
                for k in range(i-1, i+2):
                    for l in range(j-1, j+2):
                        if k == i and l == j:
                            continue
                        if k < 0 or k >= n:
                            continue
                        if l < 0 or l >= m:
                            continue
                        if board[k][l] == 1 or board[k][l] == 3:
                            cnt += 1
                if board[i][j] == 1:
                    if cnt < 2 or cnt > 3:
                        board[i][j] = 3
                else:
                    if cnt == 3:
                        board[i][j] = 2
        for i in range(n):
            for j in range(m):
                if board[i][j] == 3:
                    board[i][j] = 0
                elif board[i][j] == 2:
                    board[i][j] = 1
