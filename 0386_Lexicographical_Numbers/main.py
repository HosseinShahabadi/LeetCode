class Solution:
    def lexicalOrder(self, n: int) -> list[int]:
        ans = []
        cur_number = 1

        for _ in range(n):
            ans.append(cur_number)

            if cur_number * 10 <= n:
                cur_number *= 10
            else:
                while cur_number % 10 == 9 or cur_number >= n:
                    cur_number //= 10
                cur_number += 1

        return ans
