# My solution.
class Solution:
    def numSquares(self, n: int) -> int:
        def prime_factors(n: int) -> dict:
            i = 2
            factors = {}
            while i * i <= n:
                if n % i:
                    i += 1
                else:
                    n //= i
                    if i in factors:
                        factors[i] += 1
                    else:
                        factors[i] = 1
            
            if n > 1:
                if n in factors:
                    factors[n] += 1
                else:
                    factors[n] = 1
            
            return factors
        

        def SumTwoSquares(n: int) -> bool:
            factors = prime_factors(n)
            for k, v in factors.items():
                if k % 4 == 3 and v % 2 == 1:
                    return False
            return True


        def isLegendre(n: int) -> bool:
            power_of_4 = 1
            while power_of_4 <= n:
                j = 0
                while True:
                    num = power_of_4 * (8 * j + 7)
                    if num == n:
                        return True
                    if num > n:
                        break
                    j += 1
                power_of_4 *= 4
            
            return False
        

        if n**0.5 % 1 == 0:
            return 1
        elif SumTwoSquares(n):
            return 2
        elif not isLegendre(n):
            return 3
        else:
            return 4


# Special thanks to "sagarsindhu36" for providing this solution.
class Solution:
    def numSquares(self, n: int) -> int:     
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1

        for i in range(2, n + 1):
            min_squares = float('inf')
            for j in range(1, int(i**0.5) + 1):
                min_squares = min(min_squares, dp[i - j * j])
            dp[i] = min_squares + 1
        
        return dp[-1]
