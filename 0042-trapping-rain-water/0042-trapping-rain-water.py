class Solution:
    def trap(self, height: List[int]) -> int:
        l = len(height)
        lm = [0] * l
        rm = [0] * l
        lw = 0
        rw = 0
        for i in range(l) :
            j = -i-1
            lm[i] = lw
            rm[j] = rw
            lw = max(lw, height[i])
            rw = max(rw, height[j])
        
        ret = 0
        for i in range(l) :
            tmp = min( lm[i], rm[i] ) - height[i]
            ret += max(0, tmp)
        return ret