class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        check = [False] * len(nums)

        def dfs(path):
            if len(path) == len(nums):
                ans.append(path[:])
                return 
            for i in range(len(nums)):
                if check[i] == False:
                    path.append(nums[i])
                    check[i] = True
                    dfs(path)
                    path.pop()
                    check[i] = False
        dfs([])
        return ans