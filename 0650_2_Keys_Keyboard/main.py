class Solution:
    def minSteps(self, n: int) -> int:
        def factors(num: int) -> list[int]:
            i = 2
            factors = []
            while i * i <= num:
                if num % i:
                    i += 1
                else:
                    num //= i
                    factors.append(i)
            if num > 1:
                factors.append(num)
            return factors
        

        dp = [0] * (n + 1)
        dp[:6] = [0, 0, 2, 3, 4, 5]
        for i in range(6, n + 1):
            facts = factors(i)
            if len(facts) != 1:
                dp[i] = sum([dp[fact] for fact in facts])
            else:
                dp[i] = i

        return dp[n]
