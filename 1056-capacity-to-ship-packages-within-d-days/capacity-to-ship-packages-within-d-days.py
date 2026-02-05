class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        ans = 0
        def can_ship(x) :
            d = 1
            curr_sum = 0
            for weight in weights :
                if curr_sum + weight > x :
                    d += 1
                    curr_sum = 0
                curr_sum += weight
            return d <= days

        while left <= right :
            mid = (left + right) // 2
            if can_ship(mid) :
                ans = mid
                right = mid - 1
            else :
                left = mid + 1
        return ans