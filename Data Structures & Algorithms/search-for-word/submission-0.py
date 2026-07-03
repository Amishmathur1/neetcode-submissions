class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])
        dirr = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or r >= row or c < 0 or c >= col or
                board[r][c] != word[i] or (r, c) in path
                ):
                return False
            
            path.add((r, c))
            res = False
            for dr, dc in dirr:
                res = res or dfs(r + dr, c + dc, i + 1)
            path.remove((r, c))

            return res
        
        for r in range(row):
            for c in range(col):
                if dfs(r, c, 0):
                    return True

        return False