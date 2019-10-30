class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        base = ord('0')
        intNum1 = []
        for char in num1:
            intNum1.append(ord(char)-base)
        intNum2 = []
        for char in num2:
            intNum2.append(ord(char)-base)
        # print(intNum1, intNum2)
        # Array Mulitplication
        muls = []
        for offset, a in enumerate(intNum2[::-1]):
            digits = []
            c = 0
            digits.extend([0] * offset)
            for b in intNum1[::-1]:
                digit = (a * b + c)
                c = digit // 10
                digit = digit % 10
                digits.append(digit)
            if c != 0:
                digits.append(c)
            muls.append(digits)
        # for mul in muls:
        # 	print(mul[::-1])
        ans = []
        c = 0
        for i in range(len(muls[-1])):
            to_sum = 0
            for mul in muls:
                if i < len(mul):
                    to_sum += mul[i]
            to_sum += c
            ans.append((to_sum % 10))
            c = (to_sum // 10)
        offset = len(muls[-1])
        while c != 0:
            ans.append((c % 10))
            c = (c // 10)
            offset += 1
        if ans[-1] == 0 and len(ans) != 1:
        	return '0'
        ans = [chr(base+digit) for digit in ans]
        return ''.join(ans[::-1])
if __name__ == "__main__":
    sol = Solution()
    ans = sol.multiply('9133', '0')
    print(ans)
    print(99999*99999)



