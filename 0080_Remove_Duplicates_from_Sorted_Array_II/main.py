class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 1
        k = len(nums)
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                if count >= 2:
                    nums[i-1] = float('inf')
                    k -= 1
                count += 1
            else:
                count = 1
        nums.sort()
        return k
        