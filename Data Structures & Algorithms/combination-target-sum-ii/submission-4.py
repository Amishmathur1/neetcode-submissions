class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        
        ans = []
        nums.sort()
        visited = set()

        def dfs(start, path, summ):
            if summ == target and tuple(path) not in visited:
                visited.add(tuple(path))
                ans.append(path[:])
                return 

            if summ > target or summ < 0:
                return 
            if tuple(path) in visited:
                return

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                new_sum = summ + nums[i]
                dfs(i+1, path, new_sum)

                path.pop()
                new_sum = summ - nums[i]
        dfs(0, [], 0)
        return ans