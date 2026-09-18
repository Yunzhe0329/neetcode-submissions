class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        ROWS, COLS = len(grid), len(grid[0])
        direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        islands = 0
        def BFS(row, col):
            q = deque()
            # let other pos can BFS to visited pos so we need to set to '0'
            grid[row][col] = '0'
            q.append((row, col))

            while q:
                r, c = q.popleft()
                for dr, dc in direction:
                    br, bc = r + dr, c + dc
                    if br < 0 or bc < 0 or br >= ROWS or bc >= COLS or grid[br][bc] == '0':
                        continue
                    q.append((br, bc))
                    # let other pos can BFS to visited pos so we need to set to '0'
                    grid[br][bc] = '0'
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    BFS(r, c)
                    islands += 1
        return islands
