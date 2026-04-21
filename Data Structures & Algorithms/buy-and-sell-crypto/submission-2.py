class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right, temp, maximum = 0, 0, 0, 0
        while right < len(prices):
            if left == right:
                right += 1
            elif prices[right] >= prices[left]:
                temp = prices[right] - prices[left]
                maximum = max(maximum, temp)
                right += 1
            else:
                left = right
                temp = 0
        return maximum


        