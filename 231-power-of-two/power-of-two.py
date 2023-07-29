class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n>0:
            return 2**int((math.log10(n))/math.log10(2))==n
        