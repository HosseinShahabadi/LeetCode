class Solution:
    def checkRecord(self, n: int) -> int:
        # Notice:
        # Initially, I implemented the solution using recursion with memoization.
        # While this approach worked well for small and medium values of n, it encountered
        # a "maximum recursion depth exceeded" error for larger values of n, such as n = 10101.
        # To resolve this issue, I sought help from ChatGPT, which suggested transitioning to
        # an iterative dynamic programming solution. This new approach avoids deep recursion and
        # efficiently handles large values of n within the given constraints.

        MOD = 10**9 + 7
        
        # dp[i][j][k]: i = length, j = number of 'A's, k = number of trailing 'L's
        dp = [[[0] * 3 for _ in range(2)] for _ in range(n + 1)]
        
        # Base case: An empty record is one valid record
        dp[0][0][0] = 1
        
        for i in range(1, n + 1):
            for j in range(2):  # 0 or 1 'A'
                for k in range(3):  # 0, 1, or 2 trailing 'L'
                    # Adding 'P' to the record
                    dp[i][j][0] = (dp[i][j][0] + dp[i-1][j][k]) % MOD
                    
                    # Adding 'A' to the record (only if j < 1)
                    if j > 0:
                        dp[i][j][0] = (dp[i][j][0] + dp[i-1][j-1][k]) % MOD
                    
                    # Adding 'L' to the record (only if k < 2)
                    if k > 0:
                        dp[i][j][k] = (dp[i][j][k] + dp[i-1][j][k-1]) % MOD
        
        # Sum up all the valid records of length n
        result = 0
        for j in range(2):
            for k in range(3):
                result = (result + dp[n][j][k]) % MOD
        
        return result
