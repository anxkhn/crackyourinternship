class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(x):
            l, r = 0, len(nums)  # Change len(nums)-1 to len(nums)
            while l < r:
                m = (l + r) // 2
                if nums[m] < x:
                    l = m + 1  # Change r = m to l = m + 1
                else:
                    r = m
            return l

        l = search(target)
        r = search(target + 1) - 1

        if l <= r:
            return [l, r]
        return [-1, -1]
