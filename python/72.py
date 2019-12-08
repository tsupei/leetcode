dp = {}
class Solution(object):
    def cmp(self, word1, word2, step):
        # print(word1, word2, step)
        print(word1, word2, step)
        if word1 in dp:
            if word2 in dp[word1]:
                return dp[word1][word2]

        if not word1 and not word2:
            print('END', step)
            return step
        if not word1:
            print('END', step + len(word2))
            return step + len(word2) 
        if not word2:
            print('END', step + len(word1) )
            return step + len(word1) 

        if word1[0] == word2[0]:
            if word1 not in dp:
                dp[word1] = {}
            dp[word1][word2] = self.cmp(word1[1:], word2[1:], step)
            return dp[word1][word2]
        
        # Else
        if word1 not in dp:
            dp[word1] = {}
        
        dp[word1][word2] = min([
            self.cmp(word1[1:], word2, step+1),  # delete
            self.cmp(word1, word2[1:], step+1),  # insert
            self.cmp(word1[1:], word2[1:], step+1)  # replace.
            ])
        
        return dp[word1][word2]


    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        return self.cmp(word1, word2, 0)


if __name__ == "__main__":
    sol = Solution()
    dis = sol.minDistance("horse",
"ros")
    print(dis)