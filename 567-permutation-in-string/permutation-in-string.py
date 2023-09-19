from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
    #Method 1 (using lists)
        if len(s1) > len(s2): return False
                
        s1_count = [0] * 26
        s2_count = [0] * 26
        
        window_len = len(s1)
        
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1
    
        for j in range(window_len, len(s2)):
            if s1_count == s2_count: return True
            
            s2_count[ord(s2[j-window_len]) - ord('a')] -= 1
            s2_count[ord(s2[j]) - ord('a')] += 1
        return s1_count == s2_count     

    # Dict Method #2
        # if len(s1) > len(s2):
        #     return False
        
        # s1_counter = Counter(s1)
        # s2_counter = Counter(s2[:len(s1)])
        
        # for i in range(len(s1), len(s2)):
        #     if s1_counter == s2_counter:
        #         return True
            
        #     if s2_counter[s2[i - len(s1)]] == 1:
        #         del s2_counter[s2[i - len(s1)]]
        #     else:
        #         s2_counter[s2[i - len(s1)]] -= 1
            
        #     s2_counter[s2[i]] += 1
        
        # return s1_counter == s2_counter

    # Easy to understand (sliding window)
        # window = len(s1)
        # s1_count = Counter(s1)
        
        # for i in range(len(s2)-window+1):
        #     s2_count = Counter(s2[i:i+window])
        #     if s2_count == s1_count:
        #         return True
            
        # return False