class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        prices_len = len(prices)
        if prices_len == 0 or prices_len == 1:
            return 0
        total_profit = 0
        for i in range(0,prices_len-1):
            if prices[i+1] > prices[i]:
                total_profit += prices[i+1] - prices[i]
                
        return total_profit