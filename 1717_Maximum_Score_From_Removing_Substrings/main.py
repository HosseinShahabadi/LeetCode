class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def removeSubstrings(s: str, first: str, second: str, points: int) -> (str, int):
            stack = []
            score = 0
            
            for char in s:
                if stack and stack[-1] == first and char == second:
                    stack.pop()
                    score += points
                else:
                    stack.append(char)
            
            return ''.join(stack), score
        
        if x > y:
            # Remove "ab" first
            s, score = removeSubstrings(s, 'a', 'b', x)
            _, score2 = removeSubstrings(s, 'b', 'a', y)
        else:
            # Remove "ba" first
            s, score = removeSubstrings(s, 'b', 'a', y)
            _, score2 = removeSubstrings(s, 'a', 'b', x)
        
        return score + score2
