class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 1:
            return [[1]]
        arr = [[0 for i in range(n)] for j in range(n)]
        i = 0
        j = 0
        d = 'R'
        cnt = 1
        upper = n-1
        lower = 0
        while True:
            print(i,j)
            if arr[i][j] != 0:
                break
            arr[i][j] = cnt
            if d == 'R':
                if j+1 > upper:
                    d = 'D'
                    i += 1
                else:
                    j += 1
            elif d == 'D':
                if i+1 > upper:
                    d = 'L'
                    j -= 1
                else:
                    i += 1
            elif d == 'L':
                if j-1 < lower:
                    d = 'U'
                    i -= 1
                    lower += 1
                    upper -= 1
                else:
                    j -= 1
            elif d == 'U':
                if i-1 < lower:
                    d = 'R'
                    j += 1
                else:
                    i -= 1
            cnt += 1
        return arr


if __name__ == "__main__":
    sol = Solution()
    n = 10
    arr = sol.generateMatrix(n)
    for row in arr:
        print(row)
