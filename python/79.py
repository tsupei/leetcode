class Solution(object):
    def seek(self, board, word, i, j):
        if not word:
            return False
        if board[i][j] != word[0]:
            return False
        n = len(board)
        m = len(board[0])
        if len(word) == 1:
            if board[i][j] == word:
                return True
        else:
            tmp = board[i][j]
            board[i][j] = ''
            if i+1 < n and board[i+1][j]:
                if self.seek(board, word[1:], i+1, j):
                    return True
            if j+1 < m and board[i][j+1]:
                if self.seek(board, word[1:], i, j+1):
                    return True
            if i-1 >= 0 and board[i-1][j]:
                if self.seek(board, word[1:], i-1, j):
                    return True
            if j-1 >= 0 and board[i][j-1]:
                if self.seek(board, word[1:], i, j-1):
                    return True
            board[i][j] = tmp
        return False


    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if cell == word[0]:
                    # Start Seeking
                    if self.seek(board, word, i, j):
                        return True
        return False

if __name__ == "__main__":
    sol = Solution()
    board = [
      ['A','B','C','E'],
      ['S','F','C','S'],
      ['A','D','E','E']
    ]
    word = "ABCCED"
    flag = sol.exist(board, word)
    print(flag)