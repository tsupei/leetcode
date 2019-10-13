class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        dp = [0] * len(s)
        for i in range(1,len(s)):
            if s[i-1] == '(' and s[i] == ')':
                if i > 1:
                    dp[i] = dp[i-2] + 2
                else:
                    dp[i] = 2
            elif s[i-1] == ')' and s[i] == ')':
                if i-dp[i-1]-1 >= 0 and s[i-dp[i-1]-1] == '(':
                    if i-dp[i-1]-2 < 0:
                        dp[i] = dp[i-1] + 2
                    else:
                        dp[i] = dp[i-dp[i-1]-2] + dp[i-1] + 2
                else:
                    dp[i] = 0
            else:
                dp[i] = 0

        return max(dp)

if __name__ == "__main__":
    sol = Solution()
    #(()())
    ml = sol.longestValidParentheses("(()))())(")
    print(ml)
    ml = sol.longestValidParentheses("(()(((()")
    print(ml)
