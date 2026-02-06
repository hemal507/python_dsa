class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def get_div_sum(x) :
            return sum([math.ceil(i/x) for i in nums])
        left = 1
        right = max(nums)
        ans = float('inf')
        while left <= right :
            mid = (left + right) // 2
            if get_div_sum(mid) <= threshold :
                ans = min(ans, mid)
                right = mid - 1
            else :
                left = mid + 1
        return ans