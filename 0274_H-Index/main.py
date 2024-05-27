class Solution:
    def hIndex(self, citations: list[int]) -> int:
        n = len(citations)
        citations.sort()
        print(citations)
        for i in range(n, -1, -1):
            if n-i < n and citations[n-i] >= i:
                return i
        
        return 0
    