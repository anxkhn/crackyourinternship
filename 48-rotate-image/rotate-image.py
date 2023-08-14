class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) != 1:
            # print(matrix)
            for i in range(len(matrix)):
                for j in range(len(matrix)):
                    if i<j:
                        temp = matrix[i][j]
                        matrix[i][j] = matrix[j][i]
                        matrix[j][i] = temp
            # print(matrix)
            for i in range(len(matrix)):
                matrix[i]=matrix[i][::-1]
            # print(matrix)
