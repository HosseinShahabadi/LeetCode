class Solution:
    def sortJumbled(self, mapping: list[int], nums: list[int]) -> list[int]:
        def calcCredit(x):
            x = str(x)
            ans = 0
            for num in x:
                ans = ans * 10 + mapping[int(num)]
            return ans

        return sorted(nums, key=lambda x: calcCredit(x))
