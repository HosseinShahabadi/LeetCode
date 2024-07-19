class Solution:
    def luckyNumbers (self, matrix: list[list[int]]) -> list[int]:
        minimums = [min(row) for row in matrix]
        
        maximums = []
        n = len(matrix)
        for cl in range(len(matrix[0])):
            mx = float('-inf')
            for rw in range(n):
                mx = max(matrix[rw][cl], mx)
            maximums.append(mx)

        return [num for num in maximums if num in minimums]
