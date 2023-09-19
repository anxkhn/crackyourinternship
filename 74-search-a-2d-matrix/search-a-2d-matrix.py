class Solution:
    def check(index,c):
        return index//c, index%c
        # divmod function does the same thing.

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        l = 0
        r = (len(matrix)*len(matrix[0])) - 1

        rows =len(matrix)
        columns= len(matrix[0])

        while l <= r:
    
            mid = l + (r - l) // 2

            x,y = divmod(mid,columns)
            if matrix[x][y] == target:
                return True
    
            elif matrix[x][y] < target:
                l = mid + 1
    
            else:
                r = mid - 1
        return False