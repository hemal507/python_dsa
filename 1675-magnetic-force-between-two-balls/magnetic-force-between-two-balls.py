class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def can_place(x):
            curr_pos = position[0]
            cnt = 1
            
            for pos in position[1:]:
                if pos - curr_pos >= x:
                    cnt += 1
                    curr_pos = pos
                    if cnt == m:
                        return True
            return False

        left = 1
        right = position[-1] - position[0]
        ans = 0

        while left <= right:
            mid = (left + right) // 2            
            if can_place(mid):
                ans = mid
                left = mid + 1   # move right (maximize)
            else:
                right = mid - 1

        return ans