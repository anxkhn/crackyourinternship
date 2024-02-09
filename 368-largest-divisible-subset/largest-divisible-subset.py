class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        nums.sort()
        dictt = {}

        for num in nums:
            dictt[num] = [num]

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] % nums[i] == 0 and len(dictt[nums[i]]) >= len(dictt[nums[j]]):
                    dictt[nums[j]] = dictt[nums[i]] + [nums[j]]

        max_len = 0
        for subset in dictt.values():
            max_len = max(max_len, len(subset))

        for subset in dictt.values():
            if len(subset) == max_len:
                return subset
