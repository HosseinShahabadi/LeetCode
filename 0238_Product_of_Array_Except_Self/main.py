class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [1] * n
        product = nums[0]

        for i in range(1, n):
            result[i] = product
            product *= nums[i]
        
        product = nums[-1]
        for i in range(n-2, -1, -1):
            result[i] *= product
            product *= nums[i]
            
        return result
