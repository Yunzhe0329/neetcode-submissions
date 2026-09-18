class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        islands = 0

        def BFS(row, col):
            queue = deque()
            grid[row][col] = '0'
            queue.append((row, col))

            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    neighbor_row, neighbor_col = r + dr, c + dc
                    if neighbor_row < 0 or neighbor_col < 0 or neighbor_row >= ROWS or neighbor_col >= COLS or grid[neighbor_row][neighbor_col] == '0':
                        continue
                    queue.append((neighbor_row, neighbor_col))
                    grid[neighbor_row][neighbor_col] = '0'
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    BFS(r, c)
                    islands += 1
        return islands

