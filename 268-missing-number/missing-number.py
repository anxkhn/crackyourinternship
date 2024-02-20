class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        myset = set(nums)
        for i in range(len(nums)+1):
            if i not in myset:
                return i
