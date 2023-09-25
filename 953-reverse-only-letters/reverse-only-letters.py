class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        alp = []
        for i in range(len(s)):
            if s[i].isalpha():
                alp.append(s[i])

        result = []

        for i in range(len(s)):
            if s[i].isalpha():
                result.append(alp.pop())
            else:
                result.append(s[i])

        return "".join(result)
