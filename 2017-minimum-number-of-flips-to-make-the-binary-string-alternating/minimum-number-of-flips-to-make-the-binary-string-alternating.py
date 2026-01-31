class Solution:
    def minFlips(self, s: str) -> int:
        ds = s + s
        n = len(ds)
        p1 = ''.join(['0' if i % 2 == 0 else '1' for i in range(n)])
        p2 = ''.join(['1' if i % 2 == 0 else '0' for i in range(n)])
        d1 = 0
        d2 = 0
        left = 0 
        ans = float('inf')
        len_s = len(s)

        for right in range(len(ds)) :
            if ds[right] != p1[right] :
                d1 += 1
            if ds[right] != p2[right] :
                d2 += 1
            if right - left + 1 > len_s :
                if ds[left] != p1[left] :
                    d1 -= 1
                if ds[left] != p2[left] :
                    d2 -= 1
                left += 1
            if right - left + 1 == len_s :
                ans = min(ans, d1, d2)
        return ans