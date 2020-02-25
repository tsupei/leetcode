class Solution(object):
    dp = {}
    def uniqueWordBreak(self, s, wordDict):
        if s in self.dp:
            return self.dp[s]
        print(s)
        for word in wordDict:
            if len(word) > s:
                continue
            if s.startswith(word):
                if word == s:
                    self.dp[s] = True
                    return True
                if self.uniqueWordBreak(s[len(word):], wordDict):
                    self.dp[s] = True
                    return True
        self.dp[s] = False
        return False
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not s:
            return True
        uniqueDict = []
        for i in range(len(wordDict)):
            if not self.uniqueWordBreak(wordDict[i], wordDict[:i] + wordDict[i+1:]):
                uniqueDict.append(wordDict[i])
        print(uniqueDict)
        self.dp = {}
        return self.uniqueWordBreak(s, uniqueDict)

if __name__ == "__main__":
    sol = Solution()
    s = "aaaaaaa"
    wordDict = ["aaaa", "aaa"] 
    a = sol.wordBreak(s, wordDict)
    print(a)
