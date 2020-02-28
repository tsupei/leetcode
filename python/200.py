class Solution(object):
    def findStart(self, grid, visited, si, sj):
        n = len(grid)
        m = len(grid[0])
        for i in range(si, n):
            for j in range(sj, m):
                if grid[i][j] == "1" and not visited[i][j]:
                    return i, j
            sj = 0
        return -1, -1

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        n = len(grid)
        m = len(grid[0])
        visited = [[False for i in range(m)] for j in range(n)]
        si, sj = self.findStart(grid, visited, 0, 0)
        if si == -1 and sj == -1:
            return 0
        stk = [(si, sj)]
        num = 1
        while stk:
            i, j = stk.pop()
            if grid[i][j] == "1" and not visited[i][j]:
                visited[i][j] = True
                if i-1 >= 0:
                    stk.append((i-1, j))
                if i+1 < n:
                    stk.append((i+1, j))
                if j-1 >= 0:
                    stk.append((i, j-1))
                if j+1 < m:
                    stk.append((i, j+1))
            if not stk:
                si, sj = self.findStart(grid, visited, si, sj)
                if si == -1 and sj == -1:
                    return num
                stk.append((si, sj))
                num += 1
        return num

