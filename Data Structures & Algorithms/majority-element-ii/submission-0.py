class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        d = Counter(nums)
        n = len(nums)
        ans = []
        for key, val in d.items():
            if val > n/3:
                ans.append(key)
        
        return ans