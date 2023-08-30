class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        c, r = len(colSum), len(rowSum)
        # mat = [[0 for i in range(c)] for i in range(r)]
        mat = []  
        for i in range(r):
            row = []  
            for j in range(c):
                row.append(0)  
            mat.append(row) 

        for i in range(r):
            for j in range(c):
                rsum, csum= rowSum[i], colSum[j]
                minn = min(rsum, csum)
                mat[i][j] = minn
                rowSum[i]-=minn
                colSum[j]-=minn
        return mat
