class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L, R = 0, 1 
        profit = 0 

        for R in range(len(prices)):
            if prices[L] < prices[R]: 
                profit = max(prices[R] - prices[L], profit)
            else: 
                L = R
            R += 1
        return profit