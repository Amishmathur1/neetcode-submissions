class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = Counter(nums)
        so = sorted(d.items(), key = lambda x: x[1])
        return so[-1][0]