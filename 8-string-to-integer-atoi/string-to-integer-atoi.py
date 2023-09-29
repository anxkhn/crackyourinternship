class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        is_neg = False
        final = 0
        if s[0] == "-":
            is_neg = True
        elif s[0] == "+":
            pass
        elif s[0].isnumeric() == False:
            return 0
        else:
            final = ord(s[0]) - ord("0")
        for i in range(1,len(s)):
            if s[i].isnumeric():
                final = final*10 + ord(s[i]) - ord("0")
            else:
                break
        if is_neg:
            if final > 2147483648:
                return -2147483648

            else:
                return -final
        else:
            if final > 2147483647:
                return 2147483647
            else:
                return final