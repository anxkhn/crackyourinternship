class SubrectangleQueries:

    # def __init__(self, rectangle: List[List[int]]):
    #     self.rectangle = rectangle
    #     self.ops = []

    # def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
    #     self.ops.append((row1, col1, row2, col2, newValue))

    # def getValue(self, row: int, col: int) -> int:
    #     for row1, col1, row2, col2, val in reversed(self.ops):
    #         if row >= row1 and col >= col1 and row <= row2 and col <= col2:
    #             return val
    #     return self.rectangle[row][col]


    def __init__(self, rectangle: List[List[int]]):
        self.rec = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for r in range(row1, row2+1): 
            for c in range(col1, col2+1):
                self.rec[r][c] = newValue
        

    def getValue(self, row: int, col: int) -> int:
        return self.rec[row][col]