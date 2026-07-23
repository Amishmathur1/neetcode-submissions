class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dirs = [(-1,0),(0,1),(0,-1),(1,0)]
        visited = set()
        ans = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i,j) not in visited:
                    ans = ans + 1
                    visited.add((i,j))
                    q = deque([(i,j)])

                    while q:
                        print(1)
                        r,c = q.popleft()
                        for dr,dc in dirs:
                            nr = dr + r
                            nc = dc + c
                            if 0<=nr < rows and 0<=nc < cols and (nr,nc)not in visited and grid[nr][nc]=="1":
                                visited.add((nr,nc))
                                q.append((nr, nc))
                        
        return ans           

