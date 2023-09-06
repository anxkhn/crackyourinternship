class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        l2 = []
        for i in range(len(nums)):
            x = str(nums[i])
            l2.append(int(x[::-1]))
        set_ = set(l2+nums)
        return(len(set_))

        