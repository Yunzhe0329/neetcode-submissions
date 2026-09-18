class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        dp = prices[0]

        for price in prices:
            maxProfit = max(maxProfit, price - dp)
            dp = min(dp, price)
        return maxProfit