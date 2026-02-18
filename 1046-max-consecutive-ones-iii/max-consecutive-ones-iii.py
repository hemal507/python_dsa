class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        right = len(nums) - 1
        zero_cnt = 0
        ans = 0

        for right, num in enumerate(nums) :
            if num == 0:
                zero_cnt += 1
            while zero_cnt > k :
                if nums[left] == 0 :
                    zero_cnt -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans
