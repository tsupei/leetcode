class Solution(object):
    # Solution 1
    # def lengthOfLastWord(self, s):
    #     """
    #     :type s: str
    #     :rtype: int
    #     """
    #     if not s:
    #         return 0
    #     words = s.split(' ')
    #     words = filter(lambda x:x, words)
    #     if not words:
    #         return 0
    #     return len(words[-1])

    # Solution 2 - Faster
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = 0
        for c in s[::-1]:
            if c != ' ':
                cnt += 1
            if cnt != 0 and c == ' ':
                return cnt
        return cnt

if __name__ == "__main__":
    a = "  a   "
    sol = Solution()
    print(sol.lengthOfLastWord(a))