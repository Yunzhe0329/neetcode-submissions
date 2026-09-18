class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        def DFS(row, col):
            if row < 0 or col < 0 or row >= ROWS or col >= COLS or grid[row][col] == 0:
                return 1
            if (row, col) in visited:
                return 0
            visited.add((row, col))
            perimeter = DFS(row + 1, col) + DFS(row - 1, col) + DFS(row, col + 1) + DFS(row, col - 1)
            return perimeter
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]:
                    return DFS(r, c)
        return 0