class Solution(object):
    def combination(self, n):
        comb = []
        for a in range(1,4):
            for b in range(1,4):
                for c in range(1,4):
                    for d in range(1,4):
                        if a+b+c+d == n:
                            comb.append([a, b, c, d])
        return comb


    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) < 4:
            return []
        if len(s) > 12:
            return []
        if len(s) == 4:
            return [".".join(list(s))]

        ips = []
        combs = self.combination(len(s))
        for comb in combs:
            ip = []
            ptr = 0
            for i in comb:
                if i == 2 and s[ptr] == '0':
                    break
                if i == 3 and s[ptr] == '0':
                    break

                if int(s[ptr: ptr+i]) < 256:
                    ip.append(s[ptr: ptr+i])
                    ptr = ptr + i 
                else:
                    break
            else:
                ips.append(".".join(ip))
        return ips
        
if __name__ == "__main__":
    sol = Solution()
    ips = sol.restoreIpAddresses("255255255255")
    print(ips)
