class Solution:
    def reverse(self, x: int) -> int:
        is_negative = False
        if x < 0:
            x *= -1
            is_negative = True
        
        output = 0
        for _ in range(len(str(x))):
            output *= 10
            output += x % 10
            x = int(x / 10)

        # if output.bit_length() <= 32:
        # is a better condition and works well.
        # However, at the time I'm writing this, it won't work properly on leetcode.com.
        if output > 2147483647:
            return 0

        if is_negative:
            output *= -1
            if -2147483648 <= output:
                return output
            else:
                return 0
        else:
            return output
        