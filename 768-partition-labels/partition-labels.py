class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        max_post_dict = {}
        for i,ch in enumerate(s) :
            max_post_dict[ch] = i
        left = 0
        right = 0
        ans = []
        for i, ch in enumerate(s) :
            right = max(right, max_post_dict[ch])
            if right == i :
                ans.append(right - left + 1)
                left = i + 1
            
        return ans