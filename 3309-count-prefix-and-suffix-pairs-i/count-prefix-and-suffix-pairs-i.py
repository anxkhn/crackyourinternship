class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(word1,word2):
            l1 = len(word1)
            l2 = len(word2)
            print(word1,word2,word2[:l1],word2[l2-l1:])
            if word2[:l1] == word1 and word2[l2-l1:] == word1:
                return True
            return False
        count = 0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if isPrefixAndSuffix(words[i],words[j]):
                    count+=1
        return count
