from collections import defaultdict

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d = defaultdict(int)
        for i in nums:
            if i in d:
                return i
            else:
                d[i] += 1