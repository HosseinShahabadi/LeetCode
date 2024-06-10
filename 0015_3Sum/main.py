class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        nums.sort()
        base = 0
        ans = set()
        
        for base in range(n):
            val = nums[base]
            if base > 0 and val == nums[base - 1]:
                continue

            left = base + 1
            right = n - 1
            while left < right:
                num = nums[left] + nums[right] + val
                if num == 0:
                    ans.add((val, nums[left], nums[right]))
                    right -= 1
                    left += 1
                elif num > 0:
                    right -= 1
                else:
                    left += 1

        return list(ans)
