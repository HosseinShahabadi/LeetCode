class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        ans = []
        row_up_limit, col_up_limit, row_down_limit, col_down_limit = 0, 0, len(matrix) - 1, len(matrix[0]) - 1
        
        while row_up_limit <= row_down_limit and col_up_limit <= col_down_limit:
            # Traverse from left to right
            for col in range(col_up_limit, col_down_limit + 1):
                ans.append(matrix[row_up_limit][col])
            row_up_limit += 1
            
            # Traverse from top to bottom
            for row in range(row_up_limit, row_down_limit + 1):
                ans.append(matrix[row][col_down_limit])
            col_down_limit -= 1
            
            if row_up_limit <= row_down_limit:
                # Traverse from right to left
                for col in range(col_down_limit, col_up_limit - 1, -1):
                    ans.append(matrix[row_down_limit][col])
                row_down_limit -= 1
            
            if col_up_limit <= col_down_limit:
                # Traverse from bottom to top
                for row in range(row_down_limit, row_up_limit - 1, -1):
                    ans.append(matrix[row][col_up_limit])
                col_up_limit += 1

        return ans
