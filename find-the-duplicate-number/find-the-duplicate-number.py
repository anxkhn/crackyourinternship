class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = ans = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        while ans != slow:
            ans = nums[ans]
            slow = nums[slow]
        return ans
