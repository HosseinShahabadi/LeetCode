class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> list[list[int]]:
        ans = [[rStart, cStart]]
        row, col = rStart, cStart
        alpha = 0
        n = rows * cols

        while len(ans) < n:
            alpha += 1
            # Go Right
            for _ in range(alpha):
                col += 1
                if 0 <= col < cols and 0 <= row < rows:
                    ans.append([row, col])

            # Go Down
            for _ in range(alpha):
                row += 1
                if 0 <= col < cols and 0 <= row < rows:
                    ans.append([row, col])
            
            alpha += 1
            # Go Left
            for _ in range(alpha):
                col -= 1
                if 0 <= col < cols and 0 <= row < rows:
                    ans.append([row, col])

            # Go Up
            for _ in range(alpha):
                row -= 1
                if 0 <= col < cols and 0 <= row < rows:
                    ans.append([row, col])
            
        return ans
