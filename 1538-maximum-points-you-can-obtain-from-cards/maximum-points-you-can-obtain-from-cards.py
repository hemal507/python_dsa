class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        total_sum = sum(cardPoints)

        if n == k :
            return total_sum
        
        window = n - k
        curr_sum = sum(cardPoints[:window])
        min_sum = curr_sum

        for i in range(window, n): 
            curr_sum += cardPoints[i]
            curr_sum -= cardPoints[i-window]
            min_sum = min(min_sum, curr_sum)
        
        return total_sum - min_sum