class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        current_list = []
        def findCombination(ind: int, target: int):
            if ind == len(candidates):
                if target == 0:
                    ans.append(current_list[:])
                return
            #pick
            if candidates[ind] <= target:
                current_list.append(candidates[ind])
                findCombination(ind, target - candidates[ind])
                current_list.pop()
            #not pick
            findCombination(ind + 1, target)
        
        findCombination(0, target)
        return ans
