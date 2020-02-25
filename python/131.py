class Solution(object):
    def check(self, s):
        if s == s[::-1]:
            return True
        return False
    def sub(self, s, total):
        if total == 1:
            if self.check(s):
                return [[s]]
            return []
        if total > len(s):
            return []
        if total == len(s):
            return [list(s)]
        partition = []
        for i in range(1, len(s)):
            if self.check(s[:i]):
                for posibility in self.sub(s[i:], total-1):
                    partition.append([s[:i]]+posibility)
        return partition

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        partitions = []
        if not s:
            return []
        if len(s) == 1:
            return [[s]]
        for total in range(1, len(s)+1):
            partitions.extend(self.sub(s, total))
        return partitions


if __name__ == "__main__":
    sol = Solution()
    #print(sol.check("abcba"))
    #print(sol.per(5, 10))
    print(sol.partition("aab"))
