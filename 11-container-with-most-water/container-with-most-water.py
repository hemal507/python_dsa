class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        left = 0
        right = len(height) - 1
        while left < right :
            h = min(height[left], height[right])
            l = (right - left)
            area = h * l
            ans = max(ans, area)
            if height[left] < height[right] :
                left += 1
            else :
                right -= 1
            # print(left, right, area, ans)
        return ans