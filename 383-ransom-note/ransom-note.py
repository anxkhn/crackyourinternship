class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letter_count = {}
        for i in magazine:
            letter_count[i] = letter_count.get(i, 0) + 1         


        for i in ransomNote:
            if letter_count.get(i, 0) > 0:
                letter_count[i] -= 1
            else:
                return False
        return True