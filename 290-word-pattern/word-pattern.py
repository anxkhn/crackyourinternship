class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        def check_pattern_string(s):
            lookup = {}
            output = []
            i=0
            for c in s.split(" "):
                if c in lookup:
                    output.append(lookup[c])
                else:
                    i+=1
                    lookup[c]=i
                    output.append(i)
            return(output)
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
        return check_pattern(pattern) == check_pattern_string(s)

        