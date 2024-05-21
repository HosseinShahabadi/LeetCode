class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k = len(nums)
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                nums[i-1] = float('inf')
                k -= 1
        nums.sort()
        return k
