class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        key_map = {}
        char = 97
        for i in key:
            if i.isalpha() and i not in key_map:
                key_map[i] = chr(char)
                char+=1
        str1 = []
        for i in message:
            if i in key_map:
                str1.append(key_map[i])
            else:
                str1.append(i)
        return "".join(str1)