class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        max_heap = []
        min_heap = []
        remove_dict = defaultdict(int)
        
        def calc_median() :
            if k % 2 == 0 :
                return (-max_heap[0] + min_heap[0]) / 2
            else :
                return float(-max_heap[0])
        
        def prune(heap, is_max_heap) :            
            while heap :
                num = -heap[0] if is_max_heap else heap[0]
                if remove_dict[num] > 0 :
                    remove_dict[num] -= 1
                    heapq.heappop(heap)
                else :
                    break
                
        for i in range(k) :
            heapq.heappush(max_heap, -nums[i])
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
            if len(min_heap) > len(max_heap) :
                heapq.heappush(max_heap, -heapq.heappop(min_heap))

        max_size = len(max_heap)
        min_size = len(min_heap)
        ans = [calc_median()]

        for i in range(k, len(nums)) :
            out = nums[i - k]
            remove_dict[out] += 1

            if out <= -max_heap[0] :
                max_size -= 1
            else :
                min_size -= 1
            
            if nums[i] <= -max_heap[0] :
                heapq.heappush(max_heap, -nums[i])
                max_size += 1
            else:
                heapq.heappush(min_heap, nums[i])
                min_size += 1
            
            if max_size > min_size + 1 :
                heapq.heappush(min_heap, -heapq.heappop(max_heap))
                max_size -= 1
                min_size += 1
            elif min_size > max_size :
                heapq.heappush(max_heap, -heapq.heappop(min_heap))
                min_size -= 1
                max_size += 1
            
            prune(max_heap, True)
            prune(min_heap, False)

            ans.append(calc_median())
        
        return ans
            
