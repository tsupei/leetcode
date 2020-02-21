class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        cheapest = prices[0]
        max_profit = 0
        for price in prices[1:]:
            if price - cheapest > max_profit:
                max_profit = price - cheapest
            if price < cheapest:
                cheapest = price
        return max_profit
