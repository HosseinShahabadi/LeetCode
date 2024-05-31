class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        n = len(nums)
        if n == 2:
            return nums
        
        cache = set()
        for num in nums:
            if num in cache:
                cache.remove(num)
            else:
                cache.add(num)
        
        return list(cache)
