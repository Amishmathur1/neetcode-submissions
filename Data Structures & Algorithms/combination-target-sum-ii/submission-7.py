class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []

        def dfs(start, path, summ):
            if summ == target:
                ans.append(path[:])
                return 
            
            if summ > target or summ < 0:
                return 
            
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                
                path.append(nums[i])
                new_summ = summ + nums[i]
                dfs(i+1, path, new_summ)
                path.pop()
                new_summ = summ - nums[i]
        
        dfs(0,[],0)
        return ans