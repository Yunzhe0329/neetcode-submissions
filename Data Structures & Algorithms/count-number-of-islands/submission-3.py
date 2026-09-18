class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        islands = 0
        def BFS(row, col):
            q = deque()
            # mark visited
            grid[row][col] = '0'
            q.append((row, col))

            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    next_row, next_col = r + dr, c + dc
                    if next_row < 0 or next_col < 0 or next_row >= ROWS or next_col >= COLS or grid[next_row][next_col] == '0':
                        continue
                    q.append((next_row, next_col))
                    # mark visited
                    grid[next_row][next_col] = '0'
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    BFS(r, c)
                    islands += 1
        return islands
