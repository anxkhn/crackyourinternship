class Solution:
    def arraySign(self, nums: List[int]) -> int:
        count_neg = 0
        for i in nums:
            if i == 0:
                return 0
            elif i < 0:
                count_neg +=1
        if count_neg%2 == 0:
            return 1
        else:
            return -1
        