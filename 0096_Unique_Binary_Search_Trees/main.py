class Solution:
    def numTrees(self, n: int) -> int:
        def fact(n):
            ans = 1
            for i in range(2, n+1):
                ans *= i
            return ans

        return int(fact(2*n) / ((n+1)*(fact(n)**2)))
