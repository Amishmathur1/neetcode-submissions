class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) + 2)
        for ind in range(len(nums)-1, -1, -1):
            dp[ind] = max(nums[ind] + dp[ind+2], dp[ind+1])
        return (max(dp))