"""
Thanks to hi-malik for providing a solution with better time and space complexity.
This solution improves on the original by avoiding deep copies and using efficient state management.
"""

class Solution:
    def maxScoreWords(self, words: list[str], letters: list[str], score: list[int]) -> int:
        count = [0] * 26
        letters_count = [0] * 26
        
        for letter in letters:
            count[ord(letter) - ord('a')] += 1
        
        self.result = 0
        self.backtracking(words, score, count, letters_count, 0, 0)
        return self.result
    
    def backtracking(self, words, score, count, letters_count, pos, temp):
        for i in range(26):
            if letters_count[i] > count[i]:
                return
        
        self.result = max(self.result, temp)
        
        for i in range(pos, len(words)):
            for c in words[i]:
                letters_count[ord(c) - ord('a')] += 1
                temp += score[ord(c) - ord('a')]
            
            self.backtracking(words, score, count, letters_count, i + 1, temp)
            
            for c in words[i]:
                letters_count[ord(c) - ord('a')] -= 1
                temp -= score[ord(c) - ord('a')]
