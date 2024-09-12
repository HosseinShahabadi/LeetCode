class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        allowed_set = set(allowed)
        ans = 0

        for word in words:
            if all(char in allowed_set for char in word):
                ans += 1

        return ans
