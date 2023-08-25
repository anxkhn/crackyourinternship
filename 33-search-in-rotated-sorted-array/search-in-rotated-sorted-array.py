class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2

            # if mid points the target
            if nums[mid] == target:
                return mid

            # if left part is sorted
            if nums[low] <= nums[mid]:
                if nums[low] <= target and target <= nums[mid]:
                    # element exists
                    high = mid - 1
                else:
                    # element does not exist
                    low = mid + 1
            else:  # if right part is sorted
                if nums[mid] <= target and target <= nums[high]:
                    # element exists
                    low = mid + 1
                else:
                    # element does not exist
                    high = mid - 1
        return -1
