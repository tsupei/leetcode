class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        c = 0
        a = list(a)
        b = list(b)
        num = []
        max_len = max(len(a), len(b))
        for i in range(max_len):
            digit = c
            if len(a) - 1 - i >= 0:
                digit += int(a[len(a) - 1 - i])
            if len(b) - 1 - i >= 0:
                digit += int(b[len(b) - 1 - i])
            num.append(str(digit % 2))
            c = digit // 2
        if c != 0:
            num.append(str(c))
        return "".join(num[::-1])
if __name__ == "__main__":
    a = "11"
    b = "1"
    sol = Solution()
    print(sol.addBinary(a, b))



