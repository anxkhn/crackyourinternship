class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set() 
        while n != 1:
            sums = sum([int(digit)**2 for digit in str(n)]) 
            if sums in seen: 
                return False
            else:
                n = sums
                seen.add(n)
        return True

        