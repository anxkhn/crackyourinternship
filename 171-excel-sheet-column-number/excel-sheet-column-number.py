class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        for i in columnTitle:
            ans = ans * 26 + (ord(i)%65 + 1)
        return ans
        