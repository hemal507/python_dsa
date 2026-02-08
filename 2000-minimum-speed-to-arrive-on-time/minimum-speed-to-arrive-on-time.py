class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        # if hour <= len(dist) - 1 :
        #     return -1
        def can_reach(x) :
            h = 0
            for i in dist[:-1] :
                h += math.ceil(i / x)
            h += (dist[-1] / x)
            print(h)
            return h <= hour

        left = 1
#sum(dist) failed ex 100 000  and left over time is 0.01 , to reach speed should be 100000 * (100)
        right = 10000000    
        ans = -1
        while left <= right :
            mid = (left + right) // 2
            if can_reach(mid) :
                ans = mid
                right = mid - 1
            else :
                left = mid + 1
        return ans