class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def check_pattern(s):
            lookup = {}
            output = []
            i=0
            for c in s:
                if c in lookup:
                    output.append(lookup[c])
                else:
                    i+=1
                    lookup[c]=i
                    output.append(i)
            return(output)
        check = check_pattern(pattern)
        final = []
        for word in words:
            if check_pattern(word) == check:
                final.append(word)
        return final
