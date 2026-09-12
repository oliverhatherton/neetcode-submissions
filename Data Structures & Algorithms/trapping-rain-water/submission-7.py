class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        peak = height.index(max(height))
        water = 0

        l = 0
        for r in range(1, peak + 1):
            if height[r] < height[l]:
                water += height[l] - height[r]
            else:
                l = r

        l = len(height) - 1
        for r in range(len(height) - 2, peak - 1, -1):
            if height[r] < height[l]:
                water += height[l] - height[r]
            else:
                l = r

        return water