class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        deque = collections.deque()

        for i in range(len(nums)) :

            while deque and nums[i] > nums[deque[-1]] :
                deque.pop()
            
            deque.append(i)

            while deque and deque[0] <= i - k :
                deque.popleft()
            
            if i >= k - 1 :
                ans.append( nums[deque[0]] )
        
        return ans