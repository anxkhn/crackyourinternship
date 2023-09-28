class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
    # Singe pass
        # Using List comprehenstion
        # rows = [set() for i in range(9)]
        # cols = [set() for i in range(9)]
        # grids = [set() for i in range(9)]

        # Using defaultdict with set as the value
        rows = defaultdict(set)
        cols = defaultdict(set)
        grids = defaultdict(set)

        
        for i in range(9):
            for j in range(9):
                cur = board[i][j]
                if cur != '.':
                    k = (i // 3 ) * 3 + j // 3
                    if cur not in rows[i]:
                        rows[i].add(cur)
                    else:
                        return False
                    if cur not in cols[j]: 
                        cols[j].add(cur)
                    else:
                        return False
                    if cur not in grids[k]:
                        grids[k].add(cur)
                    else:
                        return False
        return True
        # for i in range(9):
        #     set_ = set()
        #     for j in range(9):
        #         if board[i][j].isnumeric():
        #             if board[i][j] not in set_:
        #                 set_.add(board[i][j])
        #             else:
        #                 return False
        # for i in range(9):
        #     set_ = set()
        #     for j in range(9):
        #         if board[j][i].isnumeric():
        #             if board[j][i] not in set_:
        #                 set_.add(board[j][i])
        #             else:
        #                 return False
        # for x in range(0,9,3):
        #     for y in range(0,9,3):
        #         set_ = set()
        #         for i in range(x,x+3):
        #             for j in range(y,y+3):
        #                 print(i,j)
        #                 if board[j][i].isnumeric():
        #                     if board[j][i] not in set_:
        #                         set_.add(board[j][i])
        #                     else:
        #                         return False
        # return True
