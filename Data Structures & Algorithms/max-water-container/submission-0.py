class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_area = min(heights[l], heights[r]) * (r-l)

        while l < r:  
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
            area = min(heights[l], heights[r]) * (r-l)
            max_area = max(area, max_area)
        return max_area
