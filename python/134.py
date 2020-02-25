class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        for s, init_gas in enumerate(gas):
            tank = init_gas
            cur = s
            while cur < s + len(gas):
                if cost[cur%len(gas)] > tank:
                    break
                else:
                    tank -= cost[cur%len(gas)]
                    cur += 1
                    tank += gas[cur%len(gas)]
            else:
                return s
        return -1
