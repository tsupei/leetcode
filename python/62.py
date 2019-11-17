class Solution(object):
    def factorial(self, n):
        x = 1
        for i in range(1, n+1):
            x *= i
        return x

    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return self.factorial(m + n -2) / (self.factorial(m-1) * self.factorial(n-1))

if __name__ == "__main__":
    sol = Solution()
    a = sol.uniquePaths(7, 3)
    print(a)

        