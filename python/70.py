class Solution(object):
    def c(self, n, m):
        if m == 0:
            return 1
        if m > n:
            return 0
        if m == n:
            return 1
        num = 1
        for i in range(1, n+1):
            num *= i
        for i in range(1, m+1):
            num /= i
        for i in range(1, n-m+1):
            num /= i
        return num
        
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        max_amount_2 = n // 2 + 1
        way = 0
        for i in range(max_amount_2):
            num = i + n - 2 * i
            # print(num, i)
            # print(self.c(num, i))
            way += self.c(num, i)
        return way

if __name__ == "__main__":
    sol = Solution()
    print(sol.climbStairs(35))