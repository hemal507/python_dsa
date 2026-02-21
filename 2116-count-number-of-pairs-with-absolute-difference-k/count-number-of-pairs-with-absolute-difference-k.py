class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        cnt = 0
        freq = {} 
        for num in nums :
            if num - k in freq :
                cnt += freq[num - k]
            if k + num in freq :
                cnt += freq[k + num]
            freq[num] = freq.get(num, 0) + 1
        return cnt