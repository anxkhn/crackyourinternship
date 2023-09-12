class Solution:
    def minDeletions(self, s: str) -> int:
        characterCount = Counter(s)
        frequencyCount = Counter(characterCount.values())
        maxFrequency = max(frequencyCount.keys())
        
        deleteCount = 0
        for frequency in reversed(range(1, maxFrequency + 1)):
            # if frequency appears more than once, delete one of each character with that count (except one)
            # update next frequency and keep track of deletes
            if frequencyCount[frequency] > 1:
                frequencyCount[frequency - 1] += frequencyCount[frequency] - 1
                deleteCount += frequencyCount[frequency] - 1
        
        return deleteCount