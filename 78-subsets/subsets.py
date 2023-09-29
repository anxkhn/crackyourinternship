class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def sub(i, l):
            if i == n:
                res.append(l)
                return
            sub(i + 1, l + [nums[i]]) # adding temporarily to the list (not the main list)
            sub(i + 1, l)
        sub(0,[])
        return res
