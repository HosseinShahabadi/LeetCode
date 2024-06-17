class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c ** 0.5 % 1 == 0:
            return True
        
        left, right = 1, int(c ** 0.5)
        while left <= right:
            val = left**2 + right **2 - c
            if val == 0:
                return True
            elif val > 0:
                right -= 1
            else:
                left += 1
        
        return False
