class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        lst = list(s)
        total_shift = 0

        for i in range(len(shifts) - 1, -1, -1):
            total_shift = (total_shift + shifts[i]) % 26
            lst[i] = chr(((ord(lst[i]) - ord('a') + total_shift) % 26) + ord('a'))

        return "".join(lst)
