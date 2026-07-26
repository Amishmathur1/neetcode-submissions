class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [-1] * len(s)
        def dfs(ind):

            if ind == len(s):
                return 1
            if s[ind] == '0':
                return 0
            if dp[ind] != -1:
                return dp[ind]
            cnt = dfs(ind + 1)
            if ind + 1 < len(s) and 10 <= int(s[ind:ind+2]) <= 26:
                cnt += dfs(ind+2)
            dp[ind] = cnt
            return dp[ind]

        return dfs(0)