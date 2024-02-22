class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        d1 = defaultdict(int)
        d2 = defaultdict(int)
        for a, b in trust:
            d1[b] += 1
            d2[a] += 1
        for i in range(1,n+1):
            if d1[i] == n-1 and d2[i] == 0:
                return i
        return -1