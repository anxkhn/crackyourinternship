class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closedict = {")":"(","]":"[","}":"{"}
        for i in s:
            if i in closedict:
                if stack and stack[-1] == closedict[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        if not stack:
            return True
        else:
            return False        