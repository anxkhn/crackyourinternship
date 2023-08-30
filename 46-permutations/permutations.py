class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def nextPermutation(nums: List[int]):
            i = len(nums) - 2
            while i >= 0 and nums[i] >= nums[i + 1]:
                i -= 1
            if i >= 0:
                j = len(nums) - 1
                while nums[j] <= nums[i]:
                    j -= 1
                nums[i], nums[j] = nums[j], nums[i]
            nums[i + 1:] = reversed(nums[i + 1:])
            
        final = []
        final.append(nums.copy())
        temp = nums.copy()
        nextPermutation(temp)
        while temp != nums:
            final.append(temp.copy())
            nextPermutation(temp)

        return final

