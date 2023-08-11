class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        sum = 0
        maxx = float('-inf')
        for i in nums:
            sum = max(i, sum + i)
            maxx = max(maxx, sum)

        return maxx            
                