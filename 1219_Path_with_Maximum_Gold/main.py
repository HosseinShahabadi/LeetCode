class Solution:
    def getMaximumGold(self, grid: list[list[int]]) -> int:
        DIRECTIONS = [0, 1, 0, -1, 0]
        rows = len(grid)
        cols = len(grid[0])
        ans = 0

        def DFS(grid, rows, cols, row, col):
            if row < 0 or col < 0 or row == rows or col == cols or grid[row][col] == 0:
                return 0
            max_gold = 0

            original_val = grid[row][col]
            grid[row][col] = 0

            for direction in range(4):
                max_gold = max(max_gold, DFS(grid, rows, cols,
                                                       DIRECTIONS[direction] + row,
                                                       DIRECTIONS[direction + 1] + col))

            grid[row][col] = original_val
            return max_gold + original_val

        for row in range(rows):
            for col in range(cols):
                ans = max(ans, DFS(grid, rows, cols, row, col))
        
        return ans
