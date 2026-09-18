class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS = len(board)
        COLS = len(board[0])

        # Check Rows
        for i in range(ROWS):
            hash_set = set()
            for j in range(COLS):
                item = board[i][j]
                if item in hash_set:
                    return False
                elif item != '.':
                    hash_set.add(item)
        # Check Cols
        for i in range(ROWS):
            hash_set = set()
            for j in range(COLS):
                item = board[j][i]
                if item in hash_set:
                    return False
                elif item != '.':
                    hash_set.add(item)
        # starts of sub-boxes
        starts = {
            (0, 0), (0, 3), (0, 6),
            (3, 0), (3, 3), (3, 6),
            (6, 0), (6, 3), (6, 6)
        }

        for i, j in starts:
            hash_set = set()
            for row in range(i, i + 3):
                for col in range(j, j + 3):
                    item = board[row][col]
                    if item in hash_set:
                        return False
                    elif item != '.':
                        hash_set.add(item)
        return True
                    
