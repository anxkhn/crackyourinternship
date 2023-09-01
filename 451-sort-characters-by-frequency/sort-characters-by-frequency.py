class Solution:
    def frequencySort(self, s: str) -> str:
        dicc = {}
        for i in s:
            if i not in dicc:
                dicc[i] = 1
            else:
                dicc[i] += 1
        r = sorted(dicc.items(), key=lambda x:x[1], reverse=True)
        v = ""
        for i in r:
            v += i[0]*i[1]
        return v


        