class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        grid = []
        for i in range(numRows):
            grid.append([])

        base = 0
        baseUpdater = -1
        grid[base].append(s[0])

        for i in range(1, len(s)):
            if base >= (numRows - 1) or base <= 0:
                baseUpdater *= -1
            base += baseUpdater

            grid[base].append(s[i])

        string = ''
        for i in range(numRows):
            string += ''.join(grid[i])
        return string
        