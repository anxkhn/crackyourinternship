class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans = []
        for i in range(len(nums)):
            temp = nums[i] + nums[len(nums)-i-1]
            ans.append(temp)
        return max(ans)



        