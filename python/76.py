# todo - Not complete
class Solution(object):

    def substring(self, diff_dict):
        for key, value in diff_dict.items():
            if value < 0:
                return False
        return True

    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s:
            return ""

        best_length = len(s)+1
        best_str = ""
        left = 0
        right = 0

        diff_dict = {}
        for c in t:
            if c not in diff_dict:
                diff_dict.setdefault(c, -1)
            else:
                diff_dict[c] -= 1

        while left <= right <= len(s):
            # print(left, right, diff_dict)
            if self.substring(diff_dict):
                if len(s[left:right]) < best_length:
                    best_str = s[left:right]
                    best_length = len(best_str)
                if s[left] in diff_dict:
                    diff_dict[s[left]] -= 1
                left += 1
            else:
                if right < len(s):
                    if s[right] in diff_dict:
                        diff_dict[s[right]] += 1
                right += 1
        return best_str


if __name__ == "__main__":
    sol = Solution()
    s = "ADOBECODEBANC"
    t = "ABC"

    valid = sol.minWindow(s, t)
    print(valid)
        