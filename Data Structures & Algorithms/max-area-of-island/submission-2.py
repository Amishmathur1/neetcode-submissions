class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        dic = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        row = len(grid)
        col = len(grid[0])
        max_area = 0
        
        def dfs(r, c):
            if r < 0 or r >= row or c < 0 or c >= col or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0
            area = 1

            for dr, dc in dic:
                nr = r + dr
                nc = c + dc
                area += dfs(nr, nc)
            return area
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r,c))
        
        return max_area