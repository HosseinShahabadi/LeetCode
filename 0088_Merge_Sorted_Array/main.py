class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if n != 0:
            endofnum1 = m
            maximum = len(nums1)
            num2index = 0

            for i in range(maximum):
                if i - num2index >= m:
                    for j in range(num2index, n):
                        nums1[i] = nums2[j]
                        i += 1
                    break
                elif num2index >= n:
                    break
                
                if nums1[i] > nums2[num2index]:
                    nums1[endofnum1] = nums2[num2index]
                    for j in range(endofnum1, i, -1):
                        temp = nums1[j]
                        nums1[j] = nums1[j - 1]
                        nums1[j - 1] = temp
                    
                    endofnum1 += 1
                    num2index += 1
        