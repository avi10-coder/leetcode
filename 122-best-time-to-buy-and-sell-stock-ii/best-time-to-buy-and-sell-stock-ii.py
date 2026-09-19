class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        i = 0
        curr_min = 0
        while i < len(prices)-1:
            if prices[i] >= prices[i+1]:
                profit += prices[i] - prices[curr_min]
                i += 1
                curr_min = i
            else:
                i += 1
        profit += prices[i] - prices[curr_min]
        return profit
            
        