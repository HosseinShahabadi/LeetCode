class Solution:
    def missingRolls(self, rolls: list[int], mean: int, n: int) -> list[int]:
        ntotal = mean * (len(rolls) + n) - sum([num for num in rolls])
        
        if ntotal < n or n * 6 < ntotal:
            return []
        
        p = ntotal // n
        q = ntotal % n
        ans = [p+1] * q
        ans.extend([p] * (n - q))
        
        return ans
