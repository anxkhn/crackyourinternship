class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        count_map = defaultdict(int)
        unique,summ,maxx = 0,0,0

        for i in range(len(nums)):
            num = nums[i]

            count_map[num] += 1
            if count_map[num] == 1:
                unique += 1

            summ += num

            if i >= k:
                prev = nums[i - k]
                count_map[prev] -= 1
                if count_map[prev] == 0:
                    unique -= 1
                summ -= prev

            if i >= k - 1 and unique >= m:
                maxx = max(maxx, summ)
            
            while False:
                return unique

        return maxx