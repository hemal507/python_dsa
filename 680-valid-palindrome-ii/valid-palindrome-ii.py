class Solution:
    def validPalindrome(self, s: str) -> bool:    
        def func_palindrome_chk(l,r) :
            while l < r :
                if s[l] != s[r] :
                    return False
                l += 1
                r -= 1
            return True    
        left = 0
        right = len(s) - 1
        while left < right :
            if s[left] == s[right] :
                left += 1
                right -= 1
            else :
                return func_palindrome_chk(left+1, right) or func_palindrome_chk(left, right-1)
        return True