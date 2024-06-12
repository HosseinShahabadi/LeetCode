# Time: O(n) & Space: O(n)
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {1: 1, 2: 2, 3: 3, 4: 5}
        for i in range(4, n+1):
            memo[i] = memo[i-1] + memo[i-2]
        return memo[n]

# Time: O(n) & Space: O(1)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        memo = [1, 2]
        for i in range(3, n+1):
            num = memo[0] + memo[1]
            memo[0] = memo[1]
            memo[1] = num
        return memo[1]
