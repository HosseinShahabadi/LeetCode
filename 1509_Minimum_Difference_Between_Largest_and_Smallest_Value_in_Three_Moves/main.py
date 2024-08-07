class Solution:
    def minDifference(self, nums: list[int]) -> int:
        if len(nums) <= 4:
            return 0
        
        nums.sort()

        k = len(nums) - 3
        ans = nums[-1] - nums[0]
        for i in range(k - 1, len(nums)):
            ans = min(ans, nums[i] - nums[i - k + 1])
        
        return ans
