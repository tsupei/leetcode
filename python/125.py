class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        valid = []
        s = s.lower()
        for c in s:
            if ord('a') <= ord(c) <= ord('z') or ord('0') <= ord(c) <= ord('9'):
                valid.append(c)
        total = len(valid)
        for i in range(total // 2):
            if valid[i] != valid[total-i-1]:
                return False
        return True
