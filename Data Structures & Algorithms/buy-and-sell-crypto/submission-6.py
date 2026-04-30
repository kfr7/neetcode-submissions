class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0 or len(prices) == 1:
            return 0
        l, r = 0, 0
        max_profit = 0
        while l <= r and r < len(prices):
            if l == r:
                r += 1
                continue
            if prices[r] - prices[l] > max_profit:
                max_profit = prices[r] - prices[l]
            # and then pointer arithmetic
            if prices[l] > prices[r]:
                l += 1
            else:   # the right is greater
                r += 1
        return max_profit
        