class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isValid(row):
            RowHash = {}
            for i in row:
                if i == ".":
                    continue
                if i in RowHash:
                    return False
                RowHash[i] = 1
            return True

        columns = [[] for _ in range(9)]
        grids = [[] for _ in range(9)]    

        for r in range(9):
            for c in range(9):
                val = board[r][c]  
                columns[c].append(val)   
                grid_index = (r // 3) * 3 + (c // 3)
                grids[grid_index].append(val)

        for i in range(9):
            b = isValid(board[i])
            c = isValid(columns[i])
            g = isValid(grids[i])

            if b==False or c==False or g==False:
                return False

        return True    