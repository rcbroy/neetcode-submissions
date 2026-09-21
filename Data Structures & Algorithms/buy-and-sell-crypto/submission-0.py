class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = diff = 0
        j = 1
        while j < len(prices):
            diff = max(diff, prices[j]-prices[i])
            if prices[j] < prices[i]:
                i = j
            j += 1
        return diff

            
