from collections import defaultdict
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        t_map = defaultdict(int)
        for t in tasks:
            t_map[t] += 1
        
        heap = []
        res = 0
        
        for key in t_map:
            val = t_map[key]
            # heapq is implemented as a min heap, negate val so we get a max heap
            heapq.heappush(heap, (-val, key))
        
        while heap:
            temp = []
            for i in range(n + 1):
                if len(heap) > 0:
                    popped = heapq.heappop(heap)
                    temp.append(popped)
                    
            for i in temp:
                poppedVal = -i[0]
                # if the popped val from heap > 0 we need to push it back bc there are still tasks left
                if poppedVal - 1 > 0:
                    heapq.heappush(heap, (-(poppedVal - 1), i[1]))
            if len(heap) > 0:
                res += n + 1
            else:
                res += len(temp)
        
        return res
