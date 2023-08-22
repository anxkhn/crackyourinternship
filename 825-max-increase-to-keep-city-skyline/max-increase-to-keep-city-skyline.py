class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        max_values_row = [0] * len(grid)
        for row in range(len(grid)):
            for col in range (len(grid[row])):
                if grid[row][col]>max_values_row[row]:
                    max_values_row[row]=grid[row][col]


        max_values_col = [0] * len(grid[0])
        for col in range(len(grid[0])):
            for row in range(len(grid)):
                if grid[row][col] > max_values_col[col]:
                    max_values_col[col] = grid[row][col]

        # To update to new matrix
        # for row in range(len(grid)):
        #     for col in range (len(grid[row])):
        #         x = min (max_values_row[row],max_values_col[col])
        #         if x > grid[row][col]:
        #             grid[row][col] = x

        count = 0
        for row in range(len(grid)):
            for col in range (len(grid[row])):
                x = min (max_values_row[row],max_values_col[col])
                if x > grid[row][col]:
                    count += x - grid[row][col]


        return count