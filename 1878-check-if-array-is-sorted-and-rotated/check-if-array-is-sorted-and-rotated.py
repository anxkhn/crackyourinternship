class Solution:
    def check(self, nums: List[int]) -> bool:
        i = 0
        while i < len(nums)-1:
            if nums[i+1] >= nums[i]:
                i+=1
            else:
                break
        new_arr = nums[i+1:]+nums[:i+1]
        for i in range(len(new_arr)-1):
            if new_arr[i+1] >= new_arr[i]:
                pass
            else:
                return False
        return True

                