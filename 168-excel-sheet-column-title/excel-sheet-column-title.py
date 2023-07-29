class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        word = ""
        while columnNumber > 0:
            columnNumber -= 1
            word = chr((columnNumber % 26) + 65) + word
            columnNumber //= 26
        return word
