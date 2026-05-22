class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, 1
        orig_r = 1

        while l < len(numbers):
            if r == len(numbers):
                r = orig_r + 1
                l += 1
            if target != numbers[l] + numbers[r]:
                r += 1
            else:
                return [l+1, r+1]
            
                