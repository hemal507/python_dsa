class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def func_atmostk(inp_k):
            left = 0 
            ans = 0
            d = {} 

            for right, num in enumerate(nums):
                d[num] = d.get(num,0) + 1

                while len(d) > inp_k :
                    left_num = nums[left]
                    d[left_num] -= 1

                    if d[left_num] == 0:
                        del d[left_num]
                    left += 1

                ans += (right - left + 1)
            return ans
        return func_atmostk(k) - func_atmostk(k-1)