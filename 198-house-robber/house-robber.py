class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        
        dp = [-1] * len(nums) # cache
        return self.robMax(nums, dp, len(nums) - 1)
    
    
    def robMax(self, nums, dp, i):
        if i < 0:
            return 0
        
        if dp[i] != -1: # if the value of dp[i] is not default i.e. -1 that means we have already calculated it so we dont have to do it again we just have to return it
            return dp[i]
        
        dp[i] = max(nums[i] + self.robMax(nums, dp, i - 2), self.robMax(nums, dp, i - 1))
        return dp[i]