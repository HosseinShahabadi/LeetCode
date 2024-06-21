# Big thanks to "prodonik" for coming up with this awesome solution!
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        if m < n:
            return ""

        map = [0] * 128
        start = 0
        end = 0
        min_len = float('inf')
        start_index = 0
        for char in t:
            map[ord(char)] += 1

        while end < m:
            if map[ord(s[end])] > 0:
                n -= 1
            map[ord(s[end])] -= 1
            end += 1

            while n == 0:
                if end - start < min_len:
                    start_index = start
                    min_len = end - start

                if map[ord(s[start])] == 0:
                    n += 1
                map[ord(s[start])] += 1
                start += 1

        return "" if min_len == float('inf') else s[start_index:start_index + min_len]
