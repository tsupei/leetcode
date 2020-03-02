class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        buf = []
        stk = []
        for c in s:
            if 0 <= ord(c)-ord('0') <= 9:
                buf.append(ord(c)-ord('0'))
            elif c == " ":
                continue
            else:
                # Get op1
                num = 0
                for idx, e in enumerate(buf[::-1]):
                    num += e * (10 ** idx)
                buf = []
                stk.append(num)
                stk.append(c)
        if buf:
            num = 0
            for idx, e in enumerate(buf[::-1]):
                num += e * (10 ** idx)
            buf = []
            stk.append(num)
        # print(stk)
        op1 = stk[0]
        ptr = 1
        while ptr < len(stk):
            if stk[ptr] == "+" or stk[ptr] == "-":
                if stk[ptr] == "+":
                    op = "+"
                else:
                    op = "-"
                ptr += 1
                op2 = stk[ptr]
                ptr += 1
                while ptr < len(stk):
                    if stk[ptr] == "*":
                        op2 *= stk[ptr+1]
                        ptr += 2
                    elif stk[ptr] == "/":
                        op2 /= stk[ptr+1]
                        ptr += 2
                    else:
                        break
                if op == "+":
                    op1 = op1 + op2
                else:
                    op1 = op1 - op2
            elif stk[ptr] == "*":
                ptr += 1
                op1 *= stk[ptr]
                ptr += 1
            elif stk[ptr] == "/":
                ptr += 1
                op1 /= stk[ptr]
                ptr += 1
        return op1

if __name__ == "__main__":
    sol = Solution()
    ans = sol.calculate("3+5/2*3+21")
    print(ans)

# TestCases
# 15 / 5
# 6 / 0
# 0 / 6
# 0
# 1234
# 0 * 6
# 6 / 4 * 3


