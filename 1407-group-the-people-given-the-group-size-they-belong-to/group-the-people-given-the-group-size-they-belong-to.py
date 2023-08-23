class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        progress = {}
        final = []
        
        for i in range(len(groupSizes)):
            if groupSizes[i] not in progress:
                progress[groupSizes[i]] = [i]
            else:
                progress[groupSizes[i]] += [i]

            if len(progress[groupSizes[i]]) == groupSizes[i]:
                final.append(progress.pop(groupSizes[i]))
            
        print(final)

        return final
