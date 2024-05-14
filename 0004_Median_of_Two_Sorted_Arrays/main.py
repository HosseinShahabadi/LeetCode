class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        mid = int((m + n)/2)

        if not nums1:
            if (m + n) % 2 == 0:
                return (nums2[mid - 1] + nums2[mid])/2
            else:
                return nums2[mid]
        
        if not nums2:
            if (m + n) % 2 == 0:
                return (nums1[mid - 1] + nums1[mid])/2
            else:
                return nums1[mid]
        
        
        nums1Pointer = 0
        nums2Pointer = 0

        nums3 = []

        for i in range(mid + 1):
            if nums1[nums1Pointer] > nums2[nums2Pointer]:
                nums3.append(nums2[nums2Pointer])
                nums2Pointer += 1
            else:
                nums3.append(nums1[nums1Pointer])
                nums1Pointer += 1

            if nums1Pointer >= m:
                for j in range(i + 1, mid + 1):
                    nums3.append(nums2[nums2Pointer])
                    nums2Pointer += 1
                break
            elif nums2Pointer >= n:
                for j in range(i + 1, mid + 1):
                    nums3.append(nums1[nums1Pointer])
                    nums1Pointer += 1
                break

        if (m + n) % 2 == 0:
            return (nums3[-1] + nums3[-2])/2
        else:
            return nums3[-1]