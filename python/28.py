class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        pnee = 0
        for i in range(len(haystack)):
            cur = i
            while haystack[cur] == needle[pnee]:
                cur += 1
                pnee += 1
                if pnee == len(needle):
                    return i
            pnee = 0
        return -1

if __name__ == "__main__":
    sol = Solution()
    leng = sol.strStr("mississippi", "issip")
    print(leng)