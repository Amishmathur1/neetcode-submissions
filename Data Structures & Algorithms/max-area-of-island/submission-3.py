class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        dic = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        row = len(grid)
        col = len(grid[0])
        max_area = 0

        visited = set()
        def dfs(r, c):
            stack = [[r,c]]
            visited.add((r,c))
            area = 0
            while stack:
                r, c = stack.pop()
                area += 1
                for dr, dc in dic:
                    nr, nc = dr+r, dc+c
                    if (
                        0 <= nr < row and
                        0 <= nc < col and
                        (nr,nc) not in visited and
                        grid[nr][nc] == 1
                    ):
                        visited.add((nr,nc))
                        stack.append([nr, nc])
            return area


                            
                        
            
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r,c))
        
        return max_area