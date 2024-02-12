class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        sol = None
        cnt = 0
        for i in nums:
            if cnt == 0:
                sol = i
            cnt += (1 if i == sol else -1)
        return sol
