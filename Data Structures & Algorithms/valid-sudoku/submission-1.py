class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i, row in enumerate(board):
            if not self.isValidList(row):
                return False
            col = []
            square = []
            for j, c in enumerate(row):
                col.append(board[j][i])
                x = 3 * (i//3) + j//3
                y = 3*(i%3) + (j%3)
                square.append(board[x][y])
            print(col)
            if not self.isValidList(col):
                return False
            if not self.isValidList(square):
                return False
        return True
    
    def isValidList(self, row: List[str]) -> bool:
        digits = set()
        for r in row:
            if r != '.' and r in digits:
                return False
            digits.add(r)
        return True
        