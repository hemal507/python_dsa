class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 1
        right = 0
        seen = set()
        for right in range(1,len(nums)):
            if nums[right] != nums[left - 1] :
                nums[left] = nums[right]
                left += 1
            # print(left, right, nums[left], nums[right], nums)
        return left
            