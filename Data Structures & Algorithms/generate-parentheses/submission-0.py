class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        ans = []

        def dfs(o, c):
            if o==c==n:
                ans.append(''.join(stack))
                return 
            
            if o > c:
                stack.append(')')
                dfs(o, c+1)
                stack.pop()
            if o < n:
                stack.append('(')
                dfs(o+1, c)
                stack.pop()
        
        dfs(0, 0)
        return ans