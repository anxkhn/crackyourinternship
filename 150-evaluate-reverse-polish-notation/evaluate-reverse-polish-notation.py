class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stck = []
        for i in tokens:
            if i == "+" or i == "-" or i == "*" or i == "/":
                x = stck.pop()
                y = stck.pop()
                if i == "+":
                    stck.append(int(x)+int(y))
                elif i == "-":
                    stck.append(int(y)-int(x))
                elif i == "*":
                    stck.append(int(y)*int(x))
                else:
                    stck.append(int(int(y)/int(x)))
            else:
                stck.append(int(i))
        return int(stck.pop())