class Solution:
    def chalkReplacer(self, chalk: list[int], k: int) -> int:
        total = sum([ch for ch in chalk])
        k %= total
        for index, ch in enumerate(chalk):
            if ch > k:
                return index
            else:
                k -= ch
        
        return 0
    