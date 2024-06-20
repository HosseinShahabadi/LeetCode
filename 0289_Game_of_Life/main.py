class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        def neighborsPower(i, j, n, m) -> int:
            ans = 0
            neighbors = [
                (-1, 0), (-1, -1), (-1, 1),
                (1, 0), (1, -1), (1, 1),
                (0, -1), (0, 1)
            ]
            
            for di, dj in neighbors:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n:
                    ans += board[ni][nj]

            return ans


        memo = set()
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                power = neighborsPower(i, j, n, m)
                if board[i][j]:
                    if 2 <= power <= 3:
                        memo.add((i, j))
                else:
                    if power == 3:
                        memo.add((i, j))

        for i in range(m):
            for j in range(n):
                if (i, j) in memo:
                    board[i][j] = 1
                else:
                    board[i][j] = 0
