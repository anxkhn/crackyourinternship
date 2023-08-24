class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        a = set()
        b = set()
        ans = []
        count = 0
        for i in range(0, len(A)):
            a.add(A[i])
            b.add(B[i])
            if A[i] == B[i]:
                count += 1
                ans.append(count)
                continue
            if A[i] in b:
                count += 1
            if B[i] in a:
                count += 1
            ans.append(count)
        return ans
            