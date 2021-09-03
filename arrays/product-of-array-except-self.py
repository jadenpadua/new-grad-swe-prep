class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:        
        runningProduct = 1
        output = [1] * len(nums)
        
        for i in range(len(nums)):
            output[i] *= runningProduct
            runningProduct *= nums[i]
        
        runningProduct = 1
        for i in reversed(range(len(nums))):
            output[i] *= runningProduct
            runningProduct *= nums[i]
            
        return output
