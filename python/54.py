class Solution(object):
    def counterclockwise(self, matrix):
        num_of_colums = len(matrix[0])
        num_of_rows = len(matrix)
        nmat = []
        for i in range(num_of_colums):
            nrow = []
            for j in range(num_of_rows):
                nrow.append(matrix[j][num_of_colums-i-1])
            nmat.append(nrow)
        return nmat

    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        if len(matrix) == 1:
            return matrix[0]
        return matrix[0] + self.spiralOrder(self.counterclockwise(matrix[1:]))

if __name__ == "__main__":
    sol = Solution()
    mat = [[]]
    ans = sol.spiralOrder(mat)
    print(ans)