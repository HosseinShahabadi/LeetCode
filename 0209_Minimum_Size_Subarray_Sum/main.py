class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left, total, ans = 0, 0, len(nums) + 1
        for right, val in enumerate(nums):
            total += val

            while total >= target:
                ans = min(ans, right - left + 1)
                total -= nums[left]
                left += 1

        return ans % (len(nums) + 1)
