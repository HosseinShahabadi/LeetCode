# O(n log n) time complexity:
# class Solution:
#     def hIndex(self, citations: list[int]) -> int:
#         n = len(citations)
#         citations.sort()
#         for i in range(n, -1, -1):
#             if n-i < n and citations[n-i] >= i:
#                 return i
        
#         return 0


# O(n) time complexity:
class Solution:
    def hIndex(self, citations: list[int]) -> int:
        n = len(citations)
        special_list = [0] * (n+1)

        for index, value in enumerate(citations):
            if value > n :
                special_list[n] += 1
            else:
                special_list[value] += 1
        
        total = 0
        for i in range(n, -1, -1):
            total += special_list[i]
            if total >= i:
                return i
