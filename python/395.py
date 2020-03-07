import re
class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if len(s) < k:
            return 0
        hashmap = {}
        for c in s:
            if c not in hashmap:
                hashmap[c] = 1
            else:
                hashmap[c] += 1
        delimeters = []
        for c in hashmap:
            if hashmap[c] < k:
                delimeters.append(c)
        if not delimeters:
            if len(s) >= k:
                return len(s)
        pattern = re.compile("|".join(delimeters))
        substrings = re.split(pattern, s)
        substrings = filter(lambda x:x, substrings)
        max_len = 0
        for substring in substrings:
            if len(substring) < k:
                continue
            valid_len = self.longestSubstring(substring, k)
            if valid_len > max_len:
                max_len = valid_len
        if max_len < k:
            return 0
        return max_len
