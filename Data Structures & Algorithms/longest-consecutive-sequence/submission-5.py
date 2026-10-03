class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        max_val = 0

        for i in s:
            if (i-1) not in s:
                l = 1
                while (i+l) in s:
                    l += 1
                max_val = max(max_val, l)
        return max_val