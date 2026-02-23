class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ''
        for i in range(len(s)) :
            for j in range(i, len(s)) :
                tmp = s[i:j+1]
                if tmp == tmp[::-1] :
                    if len(tmp) > len(ans) :
                        ans = tmp

        return ans