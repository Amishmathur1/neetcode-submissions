class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        used = [False] * len(nums)

        def dfs(arr):
            if len(arr) == len(nums):
                ans.append(arr[:])
                return 
            
            
            for i in range(len(nums)):
                if used[i] == False:
                    arr.append(nums[i])
                    used[i] = True
                    dfs(arr)

                    arr.pop()
                    used[i] = False
                    
        dfs([])
        return ans
