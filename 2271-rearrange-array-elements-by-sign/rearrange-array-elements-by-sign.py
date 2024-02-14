class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        for i in nums:
            if i > 0:
                pos.append(i)
            elif i < 0 :
                neg.append(i)
        io = 0
        final = []
        pos_counter = 0
        neg_counter = 0
        for i in range(len(nums)):
            if io == 0:
                final.append(pos[pos_counter])
                pos_counter += 1
                io = 1
            elif io == 1:
                final.append(neg[neg_counter])
                neg_counter += 1
                io = 0
        return final
