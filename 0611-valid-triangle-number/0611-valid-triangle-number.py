import bisect
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        result = 0
        n = len(nums)
        for i in range(n-1,1,-1):
            left = 0
            right = i - 1
            while left < right :
                if nums[left] + nums[right] > nums[i] :
                    result += (right - left)
                    right -= 1
                else :
                    left += 1

        # for i in range(n-2):
        #     for j in range(i+1,n-1) :
        #         target = nums[i] + nums[j]
        #         # for k in range(j+1,n) :
        #         #     if nums[i] + nums[j] > nums[k] :
        #         #         result += 1
        #         k = bisect.bisect_left(nums, target, lo=j+1, hi=n )
        #         result += ((k-1) - (j+1) + 1)

        return result