from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        a=list(permutations(nums))
        return a