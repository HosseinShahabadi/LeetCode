class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        def transpose(matrix, n):
            for i in range(n):
                for j in range(i, n):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        def reverse_rows(matrix, n):
            for i in range(n):
                for j in range(n // 2):
                    matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]

        n = len(matrix)
        transpose(matrix, n)
        reverse_rows(matrix, n)
