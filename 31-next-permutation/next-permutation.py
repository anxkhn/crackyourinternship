class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        if len(nums) > 1:
            i = 1
            while i !=(len(nums)) and nums[-i] <= nums[-i-1] :
                i+=1
            if i == len(nums):
                nums.sort()
            else:
                min = nums[-i]
                for num in nums[-i-1:]:
                    if num > nums[-i-1]:
                        if num < min:
                            min = num

                x = nums[-i-1:]
                x.remove(min)
                x.sort()

                nums[:] = nums[:len(nums)-i-1]+[min]+x
    
