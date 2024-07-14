class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        base = 0
        ans = nums[0] + nums[1] + nums[2]
        
        for base in range(n):
            val = nums[base]
            if ans == target:
                return ans
            elif base > 0 and val == nums[base - 1]:
                continue

            left = base + 1
            right = n - 1
            while left < right:
                num = nums[left] + nums[right] + val
                if abs(num - target) <= abs(ans - target):
                    ans = num
                
                if num > target:
                    right -= 1
                else:
                    left += 1

        return ans
