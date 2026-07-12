class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        tot = 0

        def dfs(ind, path):
            nonlocal tot
            if ind >= len(nums):
                meow = 0
                for i in path:
                    meow = (meow^i)
                tot += meow
                return 

            path.append(nums[ind])
            dfs(ind+1, path)

            path.pop()
            dfs(ind+1, path)

        dfs(0, [])
        return (tot)