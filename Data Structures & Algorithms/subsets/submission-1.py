class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def dfs(ind, path):
            if ind >= len(nums):
                ans.append(path[:])
                return 
            
            path.append(nums[ind])
            dfs(ind+1, path)
            path.pop()
            dfs(ind+1, path)
        dfs(0, [])
        return ans