# Thanks to "bhanu_bhakta" for providing this solution.
class Solution:
    def minPatches(self, nums: list[int], n: int) -> int:
        miss = 1
        ans = 0
        i = 0

        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                miss *= 2
                ans += 1

        return ans
