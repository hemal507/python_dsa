class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        left = 0
        ans = 0
        n = len(s)
        d={}
        for right, ch in enumerate(s) :
            d[ch] = d.get(ch, 0) + 1
            while len(d) == 3 :
                ans = ans + (n - right)
                d[ s[left] ] -= 1
                if d[ s[left] ] == 0:
                    del d[ s[left] ]
                left += 1
        return ans
