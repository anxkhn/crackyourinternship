from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()  # Sort the candidates to handle duplicates
        
        def findCombination(ind: int, target: int, current_list: List[int]):
            if target == 0:
                ans.append(current_list[:])
                return
            
            for i in range(ind, len(candidates)):
                if i > ind and candidates[i] == candidates[i-1]:
                    continue  # Skip duplicates to avoid duplicates in results
                if candidates[i] <= target:
                    current_list.append(candidates[i])
                    findCombination(i + 1, target - candidates[i], current_list)
                    current_list.pop()
        
        findCombination(0, target, [])
        return ans
