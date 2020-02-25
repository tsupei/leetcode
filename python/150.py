class Solution(object):
    def str2int(self, s):
        if len(s) == 1:
            return ord(s) - ord('0')
        arr = list(s)
        neg = False
        if arr[0] == "-":
            neg = True
            arr.pop(0)
        total = 0
        for i in range(len(arr)):
            total += (ord(arr[i]) - ord('0') )* pow(10, len(arr)-1-i)
        if neg:
            return total * -1
        return total

    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stk = []
        for token in tokens:
            # print(stk)
            if token in ["+", "*", "/", "-"]:
                o2 = stk.pop()
                o1 = stk.pop()
                if token == "+":
                    stk.append(o1+o2)
                elif token == "-":
                    stk.append(o1-o2)
                elif token == "*":
                    stk.append(o1*o2)
                elif token == "/":
                    if (o1 < 0 and o2 > 0) or (o1 > 0 and o2 < 0):
                        if o1 % o2 != 0:
                            stk.append(o1 // o2 + 1)
                            continue
                    stk.append(o1//o2)
            else:
                stk.append(self.str2int(token))
        if len(stk) != 1:
            print('Error')
        return stk.pop()

