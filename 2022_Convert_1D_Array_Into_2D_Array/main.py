class Solution:
    def construct2DArray(self, original: list[int], m: int, n: int) -> list[list[int]]:
        if m * n != len(original):
            return []
        
        ans = []
        for i in range(m):
            ans.append(original[i*n:n+i*n])
        return ans
