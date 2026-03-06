class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for right, num in enumerate(nums) :
            comp = target - num
            if comp in d :
                return [ d[comp], right]
            else:
                d[num] = right