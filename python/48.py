class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return [[]]
        n = len(matrix)
        for i in range(n):
            for j in range(i,n):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp
        for i in range(n):
            matrix[i] = matrix[i][::-1]
        return matrix

if __name__ == "__main__":
    sol = Solution()
    mat = [
      [1,2,3],
      [4,5,6],
      [7,8,9]
    ]
    ans = sol.rotate(mat)
    print(ans)
