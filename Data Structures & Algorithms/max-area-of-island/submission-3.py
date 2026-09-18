class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def DFS(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            return 1 + DFS(r + 1, c) + DFS(r - 1, c) + DFS(r , c + 1) + DFS(r, c - 1)
        
        res = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    res = max(res,  DFS(r, c))
        return res