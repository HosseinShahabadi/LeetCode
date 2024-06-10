class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            num = numbers[left] + numbers[right]
            if num == target:
                return [left + 1, right + 1]
            if num > target:
                right -= 1
            else:
                left += 1
