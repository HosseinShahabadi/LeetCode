class Solution:
    def maxArea(self, height: list[int]) -> int:
        n = len(height)
        if n <= 1:
            return 0
        left, right = 0, n - 1
        max_volume = (right - left) * min(height[left], height[right])

        for i in range(n-1):
            volume = (right - left) * min(height[left], height[right])
            if volume > max_volume:
                max_volume = volume
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return max_volume
