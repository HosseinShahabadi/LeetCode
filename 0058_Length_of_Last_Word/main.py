class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ans = 0
        pointer = len(s)-1
        while s[pointer] == ' ':
            pointer -= 1

        for i in range(pointer, -1, -1):
            if s[i] != ' ':
                ans += 1
            else:
                break
        
        return ans

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.strip().split()
        
        if not words:
            return 0
        
        return len(words[-1])
