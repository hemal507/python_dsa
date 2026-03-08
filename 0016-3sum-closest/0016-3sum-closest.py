class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = float('inf')
        for i in range(len(nums)) :
            left = i + 1
            right = len(nums) - 1
            while left < right :
                temp = nums[i] + nums[left] + nums[right]
                if abs(target - temp) < abs(target - ans):
                    ans = temp
                if temp < target :
                    left += 1
                elif temp > target :
                    right -= 1
                else :
                    return temp
        return ans