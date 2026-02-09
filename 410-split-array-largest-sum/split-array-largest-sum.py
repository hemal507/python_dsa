class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def can_split(x) :
            curr_sum = 0
            cnt = 1
            for i in nums :
                if curr_sum + i > x:
                    cnt += 1
                    curr_sum = i
                else :
                    curr_sum += i
            print(cnt, k)
            return cnt <= k
            
        left = max(nums)
        right = sum(nums)
        ans = -1
        while left <= right :
            mid = (left + right) // 2
            if can_split(mid) :
                ans = mid
                right = mid - 1
                print('ans', ans)
            else :
                print('left', left)
                left = mid + 1
        return ans