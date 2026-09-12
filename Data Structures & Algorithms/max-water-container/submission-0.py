class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_volume = 0

        while l < r:
            top = min(heights[l], heights[r])
            gap = r - l

            max_volume = max(max_volume, top*gap)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return max_volume
