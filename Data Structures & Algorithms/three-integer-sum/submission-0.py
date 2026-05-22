class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        i, l, r = 0, 1, len(nums)-1
        k = []

        while i < len(nums) - 1:
            if i > 0 and nums[i] == nums[i-1]:
                i += 1
                l = i + 1
                r = len(nums) - 1
                continue

            while l < r:

                total = nums[i] + nums[l] + nums[r]

                if total == 0:
                    triplet = [nums[i], nums[l], nums[r]]
                    if triplet not in k:
                        k.append(triplet)

                if total > 0:
                    r -= 1

                elif total < 0:
                    l += 1

                else:
                    l += 1
                    r -= 1

            i += 1
            l = i + 1
            r = len(nums) - 1

        return k
