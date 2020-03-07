class Solution(object):
    dp = {}
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        self.dp = {}
        return self.realCoinChange(coins, amount)

    def realCoinChange(self, coins, amount):
        if amount == 0:
            return 0
        if amount in self.dp:
            return self.dp[amount]
        min_val = -1
        for coin in coins:
            if amount - coin < 0:
                continue
            num = self.realCoinChange(coins, amount-coin)
            if num != -1:
                if min_val == -1 or num+1 < min_val:
                    min_val = num + 1
        self.dp[amount] = min_val
        return min_val




if __name__ == "__main__":
    sol = Solution()
    coins = [139,442,147,461,244,225,28,378,371]
    amount = 9914
    ans = sol.coinChange(coins, amount)
    print(ans)
