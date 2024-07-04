class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        n = len(nums)
        ans, count, left, value = 0, 0, 0, 0

        for right in range(n):
            if nums[right] % 2 == 1:
                count += 1
                value = 0

            while count == k:
                value += 1
                if nums[left] % 2 == 1:
                    count -= 1
                left += 1
            
            ans += value

        return ans
