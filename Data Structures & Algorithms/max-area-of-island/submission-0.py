class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        row = len(grid)
        col = len(grid[0])

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c):
            if r < 0 or r >= row or c < 0 or c >= col or grid[r][c] == 0:
                # count = 0
                return 0
            
            #visited condition
            grid[r][c] = 0
            area = 1
            for dr, dc in directions:
                area += dfs(r + dr, c + dc)
            return area

        max_area = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(i, j))

        return max_area
