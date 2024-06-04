class Solution:
    def longestPalindrome(self, s: str) -> int:
        n = len(s)
        ans = 0
        cache = set()
    
        for i in range(n):
            if s[i] in cache:
                ans += 2
                cache.remove(s[i])
            else:
                cache.add(s[i])

        if cache:
            ans += 1
        return ans
