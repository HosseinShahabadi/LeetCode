class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        nums.sort()
        return nums


# class Solution:
#     def sortArray(self, nums: list[int]) -> list[int]:
#         if nums:
#             pivot = nums[0]
#             lesser = self.sortArray([x for x in nums[1:] if x < pivot])
#             greater = self.sortArray([x for x in nums[1:] if x >= pivot])
#             return lesser + [pivot] + greater
#         else:
#             return []
