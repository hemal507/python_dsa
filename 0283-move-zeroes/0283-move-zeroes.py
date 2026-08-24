class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_ix = 0
        for i in range(len(nums)) :
            if nums[i] != 0:
                nums[i], nums[zero_ix] = nums[zero_ix], nums[i]
                zero_ix += 1
