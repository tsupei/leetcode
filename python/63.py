class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        dp = [[0 for i in range(m)] for j in range(n)]

        if obstacleGrid[n-1][m-1] == 1:
            return 0
        dp[n-1][m-1] = 1
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                # print("idx",i, j)
                if obstacleGrid[i][j] == 1:
                    continue
                if j+1 <m:
                    dp[i][j] += dp[i][j+1] 
                if i+1 <n:
                    dp[i][j] += dp[i+1][j]
        # for d in dp:
        #     print(d)
        return dp[0][0]


if __name__ == "__main__":
    sol = Solution()
    grid = [
        [0,0]
    ]
    a = sol.uniquePathsWithObstacles(grid)
    print(a)

