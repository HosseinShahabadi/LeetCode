class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)

        memo1 = nums[0]
        memo2 = max(memo1, nums[1])
        
        for i in range(2, n):
            memo1, memo2 = memo2, max(memo2, memo1 + nums[i])

        return memo2
