class Solution(object):
    def factorial(self, n):
        x = 1
        for i in range(1, n+1):
            x *= i
        return x

    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        if n == 1:
            return "1"

        cand = [str(i) for i in range(1,n+1)]
        arr = []
        x = self.factorial(n-1)
        # print(cand)
        while x:
            # print(n-1, k, x, arr)
            order = k // x
            k = k % x
            if k == 0:
                order -= 1
                k = x
            arr.append(cand[order])
            cand.remove(cand[order])
            n -= 1
            if n-1 == 0:
                arr = arr + cand
                break
            else:
                x = self.factorial(n-1)
        return "".join(arr)

if __name__ == "__main__":
    sol = Solution()
    arr = sol.getPermutation(1,1)
    print(arr)
    