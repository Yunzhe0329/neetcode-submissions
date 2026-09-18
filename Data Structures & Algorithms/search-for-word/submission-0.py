class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = [[False for _ in range(COLS)] for _ in range(ROWS)]

        def DFS(row, col, i):
            # equal to length of word -> can present
            if i == len(word):
                return True
            if row < 0 or col < 0 or row >= ROWS or col >= COLS or board[row][col] != word[i] or visited[row][col]:
                return False
            visited[row][col] = True
            # Go through the board[row][col]'s neighbors(4 directions)
            res = DFS(row + 1, col, i + 1) or DFS(row - 1, col, i + 1) or DFS(row, col + 1, i + 1) or DFS(row, col - 1, i + 1)
            # to avoid repeat, let others can visit
            visited[row][col] = False
            return res
        
        for row in range(ROWS):
            for col in range(COLS):
                if DFS(row, col, 0):
                    return True
        return False