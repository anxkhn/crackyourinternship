class Solution:
    def pivotInteger(self, n: int) -> int:
        left = 0
        right = (n*(n+1))//2
        i = 1
        while left <= right:
            right -= i
            if left == right:
                return i
            left += i
            i+=1
        return -1