class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        nums_dict = {}

        for num in nums:
            if num in nums_dict:
                nums_dict[num] += 1
            else:
                nums_dict[num] = 1
        
        n = n // 2
        for key, value in nums_dict.items():
            if value > n:
                return key
