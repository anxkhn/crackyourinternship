class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        lst=[]
        for i,j in c.items():
            if j>=2:
                lst.append(i)
        return lst
        