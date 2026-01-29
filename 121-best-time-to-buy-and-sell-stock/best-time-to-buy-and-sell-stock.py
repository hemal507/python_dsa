class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        buy_price = float('inf')

        for price in prices :
            buy_price = min(buy_price, price)
            ans = max(ans, price - buy_price)
        return ans