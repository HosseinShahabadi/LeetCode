class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        n, k = len(s), len(t)
        s_pointer, t_pointer = 0, 0

        while t_pointer < k and s_pointer < n:
            if s[s_pointer] == t[t_pointer]:
                t_pointer += 1
            s_pointer += 1
        return k - t_pointer
