class Solution:
    def replaceDigits(self, s: str) -> str:
        lst = list(s)
        temp = 0
        for i in range(len(lst)):
            if i % 2 != 0:
                lst[i] = chr(int(lst[i])+temp)
            else:
                temp = ord(lst[i])
        return "".join(lst)
        