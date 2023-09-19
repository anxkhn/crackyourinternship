class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        rows = len(matrix)
        columns = len(matrix[0])

        l, r = 0, rows * columns - 1

        while l <= r:
            mid = l + (r - l) // 2
            x, y = divmod(mid, columns)
            mid_val = matrix[x][y]

            if mid_val == target:
                return True
            elif mid_val < target:
                l = mid + 1
            else:
                r = mid - 1

        return False
