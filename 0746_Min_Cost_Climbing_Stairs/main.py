class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        memo = [0] * n
        memo[-1] = cost[-1]
        memo[-2] = cost[-2]
        i = n - 3
        for i in range(n-3, -1, -1):
            memo[i] = cost[i] + min(memo[i+1], memo[i+2])

        return min(memo[0], memo[1])
