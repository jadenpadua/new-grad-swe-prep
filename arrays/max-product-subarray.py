#using example [2,-3,4,-8,0]
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod, min_prod, res = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            max_case = max(nums[i], max_prod*nums[i], min_prod*nums[i])
            min_case = min(nums[i], max_prod*nums[i], min_prod*nums[i])
            max_prod, min_prod = max_case, min_case 
            res = max(max_prod, res)
        return res
