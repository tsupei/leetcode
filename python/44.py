# Failed
# import time
# class Solution(object):
#     def isMatch(self, s, p):
#         """
#         :type s: str
#         :type p: str
#         :rtype: bool
#         """
#         print(s, p)
#         time.sleep(1)
#         if not p:
#             if not s:
#                 return True
#             else:
#                 return False
#         if p and not s:
#             # if p is '*' then True
#             for c in p:
#                 if c != '*':
#                     return False
#             else:
#                 return True
#         # Check num of chars
#         cnt = 0
#         for c in p:
#             if c != '*' and c != '?':
#                 cnt += 1
#         if cnt > len(s):
#             return False
#         # Check Last
#         if p[-1] != '*' and p[-1] != '?':
#             if p[-1] != s[-1]:
#                 return False
#         if p[-1] == '?':
#             return self.isMatch(s[:-1],p[:-1])


#         if p[0] == '*':
#             rep = 0
#             for i in range(len(p)):
#                 if p[i] == '*':
#                     rep = i
#                 else:
#                     break
#             # * is at the end of pattern
#             if rep == len(p)-1:
#                 return True
#             if len(p) <= 1:
#                 return True
#             flag = False
#             for i in range(len(s)):
#                 if s[i] != p[rep+1] and p[rep+1] != '?':
#                     # Cutting
#                     continue
#                 flag = flag or self.isMatch(s[i:], p[rep+1:])
#             return flag
#         elif p[0] == '?':
#             return self.isMatch(s[1:], p[1:])
#         else:
#             if s[0] != p[0]:
#                 return False
#             else:
#             	rep = 1
#             	while rep < len(s) and rep < len(p) and s[rep] == p[rep]:
#             		rep += 1
#                 return self.isMatch(s[1:], p[1:])

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp =  [[False for i in range(len(p)+1)] for j in range(len(s)+1)]
        dp[0][0] = True
        # *****a
        for i in range(1,len(p)+1):
        	if p[i-1] == '*':
        		dp[0][i] = dp[0][i-1]
        for i in range(1,len(s)+1):
        	for j in range(1,len(p)+1):
        		if p[j-1] == '*':
        			# dp[i-1][j] ==> Match (Match any sequence)
        			# dp[i][j-1] ==> Match (Don't match anything)
        			dp[i][j] = dp[i-1][j] or dp[i][j-1]
        		else:
        			if p[j-1] == s[i-1]:
        				dp[i][j] = dp[i-1][j-1]
        			elif p[j-1] == '?':
        				dp[i][j] = dp[i-1][j-1]
        		print(i,j,dp[i][j])
        return dp[len(s)][len(p)]

if __name__ == "__main__":
    sol = Solution()
    print(sol.isMatch("aa"
,"a"))