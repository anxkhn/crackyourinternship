class Solution:
    def reverseWords(self, s: str) -> str:
        x= s.strip()
        y = x.split(" ")
        z = []
        for i in y:
            if i != '':
                z.append(i.strip())
        return " ".join(z[::-1])


        