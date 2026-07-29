class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        def dfs(ind, path):            
            if sum(path[:]) == target:
                ans.append(path[:])
                return
            if sum(path[:]) > target:
                return   
            if ind >= len(nums):
                return          

            path.append(nums[ind])
            dfs(ind, path)
            path.pop()
            dfs(ind+1, path)
        dfs(0, [])
        return ans
            
                