class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        c = 1
        ndigit = []
        for digit in digits[::-1]:
            if digit + c == 10:
                c = 1
                ndigit.append(0)
            else:
                ndigit.append(digit + c)
                c = 0

        if c == 1:
            ndigit.append(1)
        return ndigit[::-1]



if __name__ == "__main__":
    a = [9,8,9]
    sol = Solution()
    print(sol.plusOne(a))