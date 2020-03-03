class Solution(object):
    dp = {}
    def sqrt(self, x):
        low = 1
        high = x
        while high - low > 1:
            mid = (low+high) // 2
            if mid * mid > x:
                high = mid
            else:
                low = mid
        return low
            
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n in self.dp:
            return self.dp[n]
        nsqrt = self.sqrt(n)
        if nsqrt * nsqrt == n:
            return 1
        else:
            min_val = n
            for i in range(1, nsqrt+1):
                val = 1 + self.numSquares(n - i*i)
                if val < min_val:
                    min_val = val
            self.dp[n] = min_val
            return min_val
        
        
