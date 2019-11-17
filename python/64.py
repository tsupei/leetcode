class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])
   
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                # print("idx",i, j)
                if j+1<m and i+1<n:
                    grid[i][j] += min(grid[i][j+1], grid[i+1][j])
                elif j+1 <m and i+1 >=n:
                    grid[i][j] += grid[i][j+1] 
                elif i+1 <n and j+1 >=m:
                    grid[i][j] += grid[i+1][j]
        # for row in grid:
        #     print(row)
        return grid[0][0]

if __name__ == "__main__":
    sol = Solution()
    grid = [
        []
    ]
    a = sol.minPathSum(grid)
    print(a)