class Solution:
    def numTeams(self, rating: list[int]) -> int:
        n = len(rating)
        ans = 0

        for j in range(1, n - 1):
            left_smaller = left_greater = right_smaller = right_greater = 0
            rate = rating[j]

            for i in rating[:j]:
                if i < rate:
                    left_smaller += 1
                else:
                    left_greater += 1

            for k in rating[j + 1:]:
                if k < rate:
                    right_smaller += 1
                else:
                    right_greater += 1

            ans += left_smaller * right_greater + left_greater * right_smaller

        return ans
