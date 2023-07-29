class Solution:
    def minMoves(self, nums: List[int]) -> int:
        total_moves = 0
        min_num = min(nums)
        
        for num in nums:
            total_moves += num - min_num
            
        return total_moves

