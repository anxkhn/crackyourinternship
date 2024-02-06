class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set(["q","w","e","r","t","y","u","i","o","p"])
        row2 = set(["a","s","d","f","g","h","j","k","l"])
        row3 = set(["z","x","c","v","b","n","m"])
        result = []
        for word in words:
            r1=0
            r2=0
            r3=0
            for i in word:
                if i.lower() in row1:
                    r1+=1
                elif i.lower() in row2:
                    r2+=1
                elif i.lower() in row3:
                    r3+=1
            if (r1 != 0 and r2 == 0 and r3 == 0) or (r2 != 0 and r1 == 0 and r3 == 0) or (r3 != 0 and r2 == 0 and r1 == 0):
                result.append(word)
        return result
            
        