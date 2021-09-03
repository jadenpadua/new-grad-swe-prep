class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSubArr = float("-inf")
        currSubArr = float("-inf")
        for i in range(len(nums)):
            currSubArr = max(currSubArr + nums[i], nums[i])
            maxSubArr = max(maxSubArr, currSubArr)
        return maxSubArr
