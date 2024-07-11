class Solution:
    def matrixScore(self, grid: list[list[int]]) -> int:
        def toggle_row(row: int):
            for i in range(n):
                grid[row][i] = 0 if grid[row][i] else 1
        

        def toggle_col(index: int):
            for j in range(m):
                grid[j][index] = 0 if grid[j][index] else 1
        

        m, n = len(grid), len(grid[0])
        for i in range(m):
            if grid[i][0] == 0:
                toggle_row(i)
        
        for i in range(1, n):
            countone = 0
            for j in range(m):
                if grid[j][i]:
                    countone += 1
            if m/2 > countone:
                toggle_col(i)

        output = 0
        for i in range(m):
            output += int(''.join(str(v) for v in grid[i]), 2)

        return output
