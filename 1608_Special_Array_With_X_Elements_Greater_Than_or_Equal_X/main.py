class Solution:
    def specialArray(self, nums: list[int]) -> int:
        # Notice:
        # Initially, I had two answers for this problem, one with O(n^2) time complexity and 
        # another one with O(n log n) time complexity. While these solutions worked, they were 
        # not as efficient as I wanted for larger inputs.
        # I found a highly efficient O(n) time complexity solution by "hi-malik".
        # I have posted his answer here with full credits to him for his outstanding optimization.

        bucket = [0] * 1001
        
        for num in nums:
            bucket[num] += 1
        total = len(nums)
        
        for i in range(1001):
            if i == total:
                return i
            total -= bucket[i]
        
        return -1
