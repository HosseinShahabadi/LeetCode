class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        n = len(s)
        ans = ''
        for i in range(n-1, -1, -1):
            ans += (s[i] + ' ')
        return ans[:-1]
