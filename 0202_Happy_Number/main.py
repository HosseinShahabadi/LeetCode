class Solution:
    def isHappy(self, n: int) -> bool:
        memo = set()
        while not n in memo:
            memo.add(n)
            n = sum([int(num)**2 for num in str(n)])
            if n == 1:
                return True

        return False
