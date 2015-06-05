class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        prices_len = len(prices)
        if prices_len == 0 or prices_len == 1:
            return 0
        max_profit,min_price,max_price  = self.getProfit(prices)
        return max_profit
        
        
        
        
            
    def getProfit(self, prices):
        prices_len = len(prices)
        if prices_len == 1:
            return 0,prices[0],prices[0]
        
        left_max_profit,left_min_price,left_max_price = self.getProfit(prices[0:(prices_len/2)])
        right_max_profit,right_min_price, right_max_price = self.getProfit(prices[(prices_len/2):])
        
        
        max_profit = max( left_max_profit, right_max_profit, (right_max_price - left_min_price))
        min_price = min(left_min_price,right_min_price )
        max_price = max(left_max_price, right_max_price)
        
        
        return max_profit,min_price,max_price
        