class Solution:
    def longestPalindrome(self, s: str) -> str:
        # ans = ''
        # for i in range(len(s)) :
        #     for j in range(i, len(s)) :
        #         tmp = s[i:j+1]
        #         if tmp == tmp[::-1] :
        #             if len(tmp) > len(ans) :
        #                 ans = tmp

        # return ans
        start = 0 
        end = 0
        def check_pal(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r] :
                l -= 1
                r += 1
            return (l+1, r-1)
        for i in range(len(s)) :
            x, y = check_pal(i, i)
            if y - x > end - start :
                start, end = x, y

            x, y = check_pal(i, i+1)
            if y - x > end - start :
                start, end = x, y

        return s[start: end + 1]