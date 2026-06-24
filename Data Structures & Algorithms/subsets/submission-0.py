class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def dfs(ind, arr):
            nonlocal ans
            if ind >= len(nums):
                ans.append(arr[:])
                return 

            #take
            
            arr.append(nums[ind])
            dfs(ind + 1, arr)

            #not take

            arr.pop()
            dfs(ind + 1, arr)

        dfs(0, [])
        return ans