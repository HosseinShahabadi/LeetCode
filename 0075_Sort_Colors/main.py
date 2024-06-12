# O(n) Solution:
class Solution:
    def sortColors(self, nums: list[int]) -> None:
        # Do not return anything, modify nums in-place instead.
        memo = [0] * 3
        for num in nums:
            memo[num] += 1
        
        count = 0
        for i in range(3):
            nums[count:count + memo[i]] = [i] * memo[i]
            count += memo[i]

# O(n logn) Solution:
class Solution:
    def sortColors(self, nums: list[int]) -> None:
        # Do not return anything, modify nums in-place instead.
        def insertionSort(array: list[int]) -> list[int]:
            n = len(array)
            for i in range(1, n):
                insert_index = i
                current_value = array[i]
                for j in range(i-1, -1, -1):
                    if array[j] > current_value:
                        array[j+1] = array[j]
                        insert_index = j
                    else:
                        break
                array[insert_index] = current_value

        insertionSort(nums)
