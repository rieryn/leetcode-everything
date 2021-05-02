class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp = 9999999999
        maxsell = 0
        profit = 0
        minidx = 0
        maxidx=0
        for i in range(len(prices)-1):
            minp = min(minp, prices[i])
            profit = max(profit,prices[i+1]-minp)
            
        if profit < 0:
            return 0
        return profit
            
            