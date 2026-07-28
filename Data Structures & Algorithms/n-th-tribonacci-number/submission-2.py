class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [-1] * (n+2)
        def dfs(n):
            if n == 1:
                return 1
            if n == 0:
                return 0
            if n == 2:
                return 1
            if dp[n] != -1:
                return dp[n]
            
            dp[n] = dfs(n-1)+dfs(n-2)+dfs(n-3)
            return dp[n]
        return dfs(n)