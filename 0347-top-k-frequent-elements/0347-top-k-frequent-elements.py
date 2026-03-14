class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums :
            d[i] = d.get(i, 0) + 1
        d = dict( sorted(d.items(), key = lambda x : x[1], reverse=True ))
        ans = []
        i = 0
        for ky,vl in d.items() :
            ans.append(ky)
            i += 1
            if i == k :
                break
            
        return ans