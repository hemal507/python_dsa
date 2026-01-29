class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_deque = collections.deque()
        max_deque = collections.deque()

        ans = 0
        left = 0
        for right, num in enumerate(nums) :
            # print(num, min_deque, max_deque)
            while min_deque and min_deque[-1] > num :
                min_deque.pop()
            min_deque.append(num)

            while max_deque and max_deque[-1] < num :
                max_deque.pop()
            max_deque.append(num)

            while abs(max_deque[0] - min_deque[0]) > limit :
                if min_deque[0] == nums[left] :
                    min_deque.popleft()
                if max_deque[0] == nums[left] :
                    max_deque.popleft()
                left += 1
            
            ans = max(ans, right - left + 1)
        return ans