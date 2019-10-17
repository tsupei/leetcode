class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        prev = self.countAndSay(n-1)
        cur = None
        cnt = 0
        buf = []
        for c in str(prev):
            if not cur:
                cur = c
                cnt += 1
            else:
                if cur == c:
                    cnt += 1
                else:
                    buf.append(str(cnt))
                    buf.append(str(cur))
                    cur = c
                    cnt = 1
        if cnt != 0:
            buf.append(str(cnt))
            buf.append(str(cur))
        return "".join(buf)

if __name__ == "__main__":
    sol = Solution()
    print(sol.countAndSay(30))