class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k %= n
        if k == 0:
            return

        count = 0
        start = 0
        
        while count < n:
            current = start
            prev_value = nums[start]
            while True:
                next_index = (current + k) % n
                nums[next_index], prev_value = prev_value, nums[next_index]
                current = next_index
                count += 1

                if start == current:
                    break
            start += 1
