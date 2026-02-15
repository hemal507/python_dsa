class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        ans = float('-inf')

        while left < right :
            w = right - left
            l = min(height[left], height[right])
            ans = max(ans, (l * w))
            if height[left] < height[right] :
                left += 1
            else:
                right -= 1
        return ans