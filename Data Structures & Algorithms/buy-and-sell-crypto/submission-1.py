class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        least = prices[0]
        for i in range(1,len(prices)):
            curr_profit = prices[i]-least
            if curr_profit > profit:
                profit = curr_profit
            if least > prices[i]:
                least = prices[i]

        return profit


        