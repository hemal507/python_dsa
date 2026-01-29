class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        incr_dq = collections.deque()
        decr_dq = collections.deque()

        left = 0
        ans = 0

        for right, num in enumerate(nums) :
            while incr_dq and incr_dq[-1] > num :
                incr_dq.pop()
            incr_dq.append(num)
            while decr_dq and decr_dq[-1] < num :
                decr_dq.pop()
            decr_dq.append(num)

            while abs(decr_dq[0] - incr_dq[0]) > limit :
                if incr_dq[0] == nums[left] :
                    incr_dq.popleft()
                if decr_dq[0] == nums[left] :
                    decr_dq.popleft()
                left += 1
            ans = max(ans, right - left + 1)
        return ans