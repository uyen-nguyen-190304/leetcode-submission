class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Number of days n 
        n = len(prices)

        # Create a DP array OPT
        # OPT[i] = best that we can do till day i
        OPT = [0] * (n + 1)
        
        # Base case: Day 0 -> nothing so far
        OPT[0] = 0

        min_price_so_far = prices[0]
        # Recursive formula: either do nothing or sell (if already buy)
        for i in range(1, n + 1):
            # Fill the DP array
            price_today = prices[i - 1]
            OPT[i] = max(OPT[i - 1], price_today - min_price_so_far)

            # Update the min_prices_so_far if applicable
            if price_today < min_price_so_far:
                min_price_so_far = price_today

        # Return the best possible profit
        return OPT[n]