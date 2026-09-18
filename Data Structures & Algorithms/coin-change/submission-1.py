class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # create a dp list to store recent combinations
        # init value should > target amount
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for j in range(coin, amount + 1):
                if j - coin >= 0:
                    dp[j] = min(dp[j], 1 + dp[j - coin])
        return dp[amount] if dp[amount] != amount + 1 else -1