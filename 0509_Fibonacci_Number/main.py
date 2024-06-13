class Solution:
    def fib(self, n: int) -> int:
        if not n:
            return 0
        
        memo = [0, 1, 1]
        num = 1
        for i in range(3, n + 1):
            num = memo[-1] + memo[-2]
            memo[-2] = memo[-1]
            memo[-1] = num
        
        return num
