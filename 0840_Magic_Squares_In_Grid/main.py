class Solution:
    def numMagicSquaresInside(self, grid: list[list[int]]) -> int:
        def checkSquare(row, col) -> bool:
            new_grid = [grid[row][col:col+3], grid[row+1][col:col+3], grid[row+2][col:col+3]]
            seen = [False] * 10
            for i in range(3):
                for j in range(3):
                    num = new_grid[i][j]
                    if num < 1 or num > 9:
                        return False
                    if seen[num]:
                        return False
                    seen[num] = True

            if 15 != sum(new_grid[0]) or 15 != sum(new_grid[1]) or 15 != sum(new_grid[2]):
                return False
            
            col1 = new_grid[0][0] + new_grid[1][0] + new_grid[2][0]
            col2 = new_grid[0][1] + new_grid[1][1] + new_grid[2][1]
            col3 = new_grid[0][2] + new_grid[1][2] + new_grid[2][2]
            if 15 != col1 or 15 != col2 or 15 != col3:
                return False

            if 15 == new_grid[0][0] + new_grid[1][1] + new_grid[2][2]:
                if 15 == new_grid[2][0] + new_grid[1][1] + new_grid[0][2]:
                    return True
            
            return False
        
        
        ans = 0
        n, m = len(grid), len(grid[0])
        if n < 3 or m < 3:
            return 0
        
        for row in range(n-2):
            for col in range(m-2):
                if checkSquare(row, col):
                    ans += 1

        return ans
