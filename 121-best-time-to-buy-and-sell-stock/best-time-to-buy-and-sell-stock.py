class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        buy_price = float('inf')
        sell_price = float('-inf')

        for price in prices :
            buy_price = min(buy_price, price)
            sell_price = max(price, buy_price)
            ans = max(ans, sell_price - buy_price)
        return ans