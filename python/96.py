dp = {}
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n in dp:
            return dp[n]
        total = 0
        for root in range(1, n+1):
            total += (self.numTrees(root - 1) * self.numTrees(n-root))
        if n not in dp:
            dp[n] = total
        return total

if __name__ == "__main__":
    sol = Solution()
    total = sol.numTrees(3)
    print(total)