# Time: O(n) & Space: O(1)
class Solution:
    def tribonacci(self, n: int) -> int:
        memo = [0, 1, 1]
        if n <= 2:
            return memo[n]
        
        for i in range(3, n+1):
            num = sum(memo)
            memo[0] = memo[1]
            memo[1] = memo[2]
            memo[2] = num

        return num
