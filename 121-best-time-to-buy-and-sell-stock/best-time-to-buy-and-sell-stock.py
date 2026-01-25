class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy, sell  = 0, 1

        while sell < len(prices):
            if prices[buy] < prices[sell]:
                profit = prices[sell] - prices[buy]
                if profit > max_profit:
                    max_profit = profit
            else:
                buy = sell
            sell = sell + 1

        return max_profit