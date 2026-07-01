class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        perm = []
        d = Counter(nums)

        def dfs():

            if len(perm) == len(nums):
                ans.append(perm[:])
                return 
            
            for i in d:
                if d[i] > 0:
                    perm.append(i)
                    d[i] -= 1

                    dfs()

                    d[i] += 1
                    perm.pop()
                    
        dfs()
        return ans