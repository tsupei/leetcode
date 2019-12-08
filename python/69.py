# SLOW
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        rec = 1
        cnt = 1
        while cnt < x:
            cnt *= 2 * 2
            rec *= 2
        lower = rec / 2
        upper = rec

        cur = lower
        while cur * cur <= x:
            cur += 1
        return cur-1

if __name__ == "__main__":
    sol = Solution()
    a = sol.mySqrt(199)
    print(a)

