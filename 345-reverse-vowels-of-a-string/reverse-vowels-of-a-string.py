class Solution:
    def reverseVowels(self, s: str) -> str:
        stack = []
        vowels = set(["a","e","i","o","u","A","E","I","O","U"])
        for i in s:
            if i in vowels:
                stack.append(i)
        new_string = []
        for i in s:
            if i in vowels:
                new_string.append(stack.pop())
            else:
                new_string.append(i)
        return "".join(new_string)