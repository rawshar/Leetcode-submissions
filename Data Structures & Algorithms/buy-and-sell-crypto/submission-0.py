'''
two pointer will be there 
diff of both will be profit
will move the left pointer when we find the minimum
profit will be the max of the prev profit and the current profit at the day

'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxProfit=0
        lp=prices[0]
        for price in prices:
            if lp>price:
                lp=price
            else:
                maxProfit=max(maxProfit,price-lp)
        return maxProfit if len(prices)>1 else 0
        