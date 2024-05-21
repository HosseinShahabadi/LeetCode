class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        k = 0
        for num in nums:
            if num == val:
                k += 1

        if k == n:
            return 0

        pointer = -1
        for i in range(0, n):
            if nums[i] == val:
                while nums[pointer] == val:
                    pointer -= 1
                nums[i] = nums[pointer]
                nums[pointer] = val
                pointer -= 1
            if i + 1 >= n - k:
                break
        
        return n - k
