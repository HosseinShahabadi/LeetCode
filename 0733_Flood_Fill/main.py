class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        def recursive(row, col, basecolor):
            image[row][col] = color
            if row + 1 < m and image[row+1][col] == basecolor:
                recursive(row+1, col, basecolor)
            if 0 <= row - 1 and image[row-1][col] == basecolor:
                recursive(row-1, col, basecolor)
            if col + 1 < n and image[row][col+1] == basecolor:
                recursive(row, col+1, basecolor)
            if 0 <= col - 1 and image[row][col-1] == basecolor:
                recursive(row, col-1, basecolor)
            return 0
        

        m = len(image)
        n = len(image[0])
        basecolor = image[sr][sc]
        if color == basecolor:
            return image
        
        recursive(sr, sc, image[sr][sc])
        return image
