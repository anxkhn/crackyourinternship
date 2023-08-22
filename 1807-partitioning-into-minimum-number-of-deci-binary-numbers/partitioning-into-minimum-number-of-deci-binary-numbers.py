class Solution:
    def minPartitions(self, n: str) -> int:
        maxx = 0
        for i in n:
            if int(i) > maxx:
                maxx = int(i)
        return maxx