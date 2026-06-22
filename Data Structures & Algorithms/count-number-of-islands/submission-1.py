class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        row = len(grid)
        col = len(grid[0])
        count = 0

        def dfs(r, c):
            nonlocal row, col
                      
            if r < 0 or r >= row or c < 0 or c >= col or grid[r][c] == '0':
                return 
            
            grid[r][c] = '0'

            for dr,dc in directions:
                nr = r + dr
                nc = c + dc

                dfs(nr, nc)
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i, j)
        
        return count