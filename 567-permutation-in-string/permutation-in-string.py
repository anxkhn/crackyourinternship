class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = len(s1)
        s1_count = Counter(s1)
        
        for i in range(len(s2)-window+1):
            s2_count = Counter(s2[i:i+window])
            if s2_count == s1_count:
                return True
            
        return False