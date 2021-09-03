# Using [3,4,7,2,-3,1,4,2], k = 7
from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ht = defaultdict(lambda: 0)
        ht[0] = 1
        runningSum = 0
        count = 0
        for i in range(len(nums)):
            runningSum += nums[i]
            prevSumToFind = runningSum - k
            
            if prevSumToFind in ht:
                count += ht[prevSumToFind]
                
            ht[runningSum] += 1
            
        return count
