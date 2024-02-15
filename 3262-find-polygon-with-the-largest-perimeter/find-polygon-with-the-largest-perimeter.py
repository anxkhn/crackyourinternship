class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        val = sum(nums)
        for i in range(len(nums)-1,-1,-1):
            val -= nums[i]
            if val > nums[i]:
                return(val+nums[i])
        return -1