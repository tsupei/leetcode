class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n == 1:
            return x
        if n == -1:
            return 1/x
        half = self.myPow(x, n//2)
        if n % 2 == 1:
            return half * half * x
        else:
            return half * half


if __name__ == "__main__":
	x = 99.00
	n = pow(2,31)-1
	print(n)
	sol = Solution()
	ans = sol.myPow(x,n)
	print(type(ans))
	print(ans)