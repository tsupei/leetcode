class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st = 0
        for i in range(len(s)):
            if s[i] != " ":
                st = i
                break
        s = s[st:]

        et = len(s) - 1
        for j in range(len(s)):
            j = len(s) - 1 - j
            if s[j] != " ":
                et = j
                break
        s = s[:et+1]

        if len(s) == 1 and s == ".":
            return False
        if s[-2:] == "-.":
            return False
        if s[-2:] == "+.":
            return False

        if "e" in s:
            eindex = 0
            for i in range(len(s)):
                if s[i] == "e":
                    eindex = i
                    break
            if eindex == 0:
                return False
            flag = 0
            ok = [".", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "-"]
            if eindex == 1 and s[0] == ".":
                return False
            for i in range(0, eindex):
                if s[i] not in ok:
                    return False
                if s[i] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                    ok = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
                elif s[i] == ".":
                    if flag == 1:
                        return False
                    flag = 1
                    ok = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
                elif s[i] in ["+", "-"]:
                    if i == eindex-1:
                        return False
                    ok = [".", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
                else:
                    return False
            if eindex == len(s)-1:
                return False
            ok = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "-"]
            for i in range(eindex+1, len(s)):
                if s[i] not in ok:
                    return False
                if s[i] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                    ok = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
                elif s[i] in ["+", "-"]:
                    if i == len(s)-1:
                        return False
                    ok = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
                else:
                    return False
            return True

        ok = [".", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "-"]
        flag = 0
        for i in range(len(s)):
            if s[i] not in ok:
                return False
            if s[i] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                ok = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
            elif s[i] == ".":
                if flag == 1:
                    return False
                flag = 1
                ok = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
            elif s[i] in ["+", "-"]:
                if i == len(s)-1:
                    return False
                ok = [".", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
            else:
                return False
        return True


if __name__ == "__main__":
    s = " .+"
    sol = Solution()
    a = sol.isNumber(s)
    print(a)

 




