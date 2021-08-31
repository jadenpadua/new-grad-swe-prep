class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ht = {}
        for i in range(len(nums)):
            targetSum = target - nums[i]
            if targetSum in ht:
                return [ht[targetSum], i]
            ht[nums[i]] = i
