class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        left = 0
        right = len(nums)-1
        ans = 0
        curr_sum = 0
        while left < right :            
            curr_sum = nums[left] + nums[right]
            ans = max(ans, curr_sum)
            left += 1
            right -= 1
        return ans