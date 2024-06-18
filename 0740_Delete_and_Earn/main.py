class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        nums_kv = [0] * (max(nums) + 1)
        for num in nums:
            nums_kv[num] += num

        dp1 = 0
        dp2 = nums_kv[1]

        n = len(nums_kv)
        for k in range(2, n):
            dp1, dp2 = dp2, max(nums_kv[k] + dp1, dp2)

        return dp2
