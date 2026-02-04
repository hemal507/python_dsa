class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def func_bs(is_lower) :
            left = 0
            right = len(nums) - 1
            ans = -1
            while left <= right :
                mid = (left + right) // 2
                if nums[mid] == target :
                    ans = mid
                    if is_lower :
                        right = mid - 1
                    else :
                        left = mid + 1
                elif nums[mid] > target :
                    right = mid - 1
                else :
                    left = mid + 1
            return ans
        return [func_bs(True), func_bs(False)]