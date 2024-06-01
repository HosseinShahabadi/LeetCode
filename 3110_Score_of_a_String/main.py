class Solution:
    def scoreOfString(self, s: str) -> int:
        n = len(s)
        result = 0
        previous_ord = ord(s[0])
        for i in range(1, n):
            result += abs(previous_ord - ord(s[i]))
            previous_ord = ord(s[i])

        return result
