class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_eat(x) :
            hrs_needed = 0
            for pile in piles :
                hrs_needed += math.ceil(pile / x)
            return hrs_needed <= h
        left = 1
        right = max(piles)
        ans = 0
        while left <= right :
            mid = (left + right) // 2
            if can_eat(mid) :
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans