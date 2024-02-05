class Solution:
    def firstUniqChar(self, s: str) -> int:
        dicc = Counter(s)
        for i in range(len(s)):
            if dicc[s[i]] == 1:
                return i
        return -1