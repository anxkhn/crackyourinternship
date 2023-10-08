class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dict_s = {}
        dict_e = {}
        for i in range(len(s)):
            if s[i] not in dict_s:
                dict_s[s[i]] = i
            dict_e[s[i]] = i

        main = []
        start = 0
        end = 0
        for i in range(len(s)):
            end = max(end, dict_e[s[i]])
            if i == end:
                main.append(end - start + 1)
                start = i + 1

        return main
