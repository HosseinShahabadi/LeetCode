class Solution:
    def trap(self, height: list[int]) -> int:
        # Credit: The original solution was provided by Mohammed_Raziullah_Ansari.
        # It has been optimized slightly to prevent an extra loop.
        # Your contribution is greatly appreciated. Thank you!
        n = len(height)
        if n == 0:
            return 0
        
        left = [0] * n
        right = [0] * n
        
        # Fill right array
        right[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right[i] = max(right[i + 1], height[i])

        # Calculate trapped water
        left[0] = height[0]
        trappedWater = min(left[0], right[0]) - height[0]
        for i in range(1, n):
            left[i] = max(left[i - 1], height[i])
            trappedWater += min(left[i], right[i]) - height[i]
        
        return trappedWater
