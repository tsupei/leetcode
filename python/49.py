class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        group = {}
        for s in strs:
            code = 0
            key = "".join(sorted(list(s)))
            if not group.get(key):
                group[key] = [s]
            else:
                group[key].append(s)
        return group.values()


if __name__ == "__main__":
    sol = Solution()
    strs = ["cab","tin","pew","duh","may","ill","buy","bar","max","doc"]
    g = sol.groupAnagrams(strs)
    print(g)