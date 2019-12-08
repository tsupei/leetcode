class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        rec_row = [False] * m
        rec_col = [False] * n

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rec_row[i] = True
                    rec_col[j] = True
        for i in range(m):
            if rec_row[i]:
                for j in range(n):
                    matrix[i][j] = 0
        for j in range(n):
            if rec_col[j]:
                for i in range(m):
                    matrix[i][j] = 0



        return matrix

if __name__ == "__main__":
    sol = Solution()
    mat = [
      [0,1,2,0],
      [3,4,5,2],
      [1,3,1,5]
    ]
    sol.setZeroes(mat)
    print(mat)



