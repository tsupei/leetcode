class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) != len(s3):
            return False

        s1 = " " + s1
        s2 = " " + s2
        dp = [[False for i in range(len(s2))] for j in range(len(s1))]
        dp[0][0] = True

        for i in range(len(s1)):
            for j in range(len(s2)):
                sptr = i + j - 1
                # print(i, s1[i], j, s2[j], sptr, s3[sptr])
                if i != 0 and (s1[i] == s3[sptr] and dp[i-1][j]):
                    dp[i][j] = True
                if j != 0 and (s2[j] == s3[sptr] and dp[i][j-1]):
                    dp[i][j] = True

        return dp[len(s1)-1][len(s2)-1]


if __name__ == "__main__":
    sol = Solution()
    s1 = "a"
    s2 = ""
    s3 = "a"
    a = sol.isInterleave(s1, s2, s3)
    print(a)
