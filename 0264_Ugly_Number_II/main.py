class Solution:
    def nthUglyNumber(self, n: int) -> int:
        def isUgly(num: int) -> bool:
            i = 2
            factors = {2, 3, 5}
            while i * i <= num:
                if num % i:
                    i += 1
                else:
                    num //= i
                    factors.add(i)
            if num > 1:
                factors.add(num)
            return True if len(factors) == 3 else False


        count, ans = 1, 1
        i = 2
        while count != n:
            if isUgly(i):
                ans = i
                count += 1
            i += 1
        
        return ans


# This answer is from the "LeetCode" editorial.
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_numbers = [0] * n
        ugly_numbers[0] = 1

        index_multiple_of_2, index_multiple_of_3, index_multiple_of_5 = 0, 0, 0
        next_multiple_of_2, next_multiple_of_3, next_multiple_of_5 = 2, 3, 5

        for i in range(1, n):
            next_ugly_number = min(
                [next_multiple_of_2, next_multiple_of_3, next_multiple_of_5]
            )
            ugly_numbers[i] = next_ugly_number

            if next_ugly_number == next_multiple_of_2:
                index_multiple_of_2 += 1
                next_multiple_of_2 = ugly_numbers[index_multiple_of_2] * 2
            if next_ugly_number == next_multiple_of_3:
                index_multiple_of_3 += 1
                next_multiple_of_3 = ugly_numbers[index_multiple_of_3] * 3
            if next_ugly_number == next_multiple_of_5:
                index_multiple_of_5 += 1
                next_multiple_of_5 = ugly_numbers[index_multiple_of_5] * 5

        return ugly_numbers[n - 1]
