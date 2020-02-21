class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        stock = prices[0]
        profit = 0
        for price in prices[1:]:
            if price > stock:
                profit += price - stock
            stock = price
        return profit
