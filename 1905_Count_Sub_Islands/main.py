class Solution:
    def countSubIslands(self, grid1: list[list[int]], grid2: list[list[int]]) -> int:
        def floodFill(image: list[list[int]], sr: int, sc: int) -> int:
            def recursive(row, col):
                flag = True
                image[row][col] = 3
                if row + 1 < m:
                    if image[row+1][col] == 1:
                        flag = False
                        recursive(row+1, col)
                    elif image[row+1][col] == 2:
                        if not recursive(row+1, col):
                            flag = False

                if 0 <= row - 1:
                    if image[row-1][col] == 1:
                        flag = False
                        recursive(row-1, col)
                    elif image[row-1][col] == 2:
                        if not recursive(row-1, col):
                            flag = False

                if col + 1 < n:
                    if image[row][col+1] == 1:
                        flag = False
                        recursive(row, col+1)
                    elif image[row][col+1] == 2:
                        if not recursive(row, col+1):
                            flag = False

                if 0 <= col - 1:
                    if image[row][col-1] == 1:
                        flag = False
                        recursive(row, col-1)
                    elif image[row][col-1] == 2:
                        if not recursive(row, col-1):
                            flag = False

                return flag
            

            m = len(image)
            n = len(image[0])
            return 1 if recursive(sr, sc) else 0
        
        
        m = len(grid1)
        n = len(grid1[0])
        for row in range(m):
            for col in range(n):
                if grid1[row][col] and grid2[row][col]:
                    grid2[row][col] = 2
        
        ans = 0
        for row in range(m):
            for col in range(n):
                if grid2[row][col] == 2:
                    ans += floodFill(grid2, row, col)
        
        return ans
