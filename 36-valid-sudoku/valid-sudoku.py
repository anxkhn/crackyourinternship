class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            set_ = set()
            for j in range(9):
                if board[i][j].isnumeric():
                    if board[i][j] not in set_:
                        set_.add(board[i][j])
                    else:
                        return False
        for i in range(9):
            set_ = set()
            for j in range(9):
                if board[j][i].isnumeric():
                    if board[j][i] not in set_:
                        set_.add(board[j][i])
                    else:
                        return False
        for x in range(0,9,3):
            for y in range(0,9,3):
                set_ = set()
                for i in range(x,x+3):
                    for j in range(y,y+3):
                        print(i,j)
                        if board[j][i].isnumeric():
                            if board[j][i] not in set_:
                                set_.add(board[j][i])
                            else:
                                return False
        return True
