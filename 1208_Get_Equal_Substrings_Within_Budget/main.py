class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        maximum_window = 0
        current_cost = 0
        end = 0
        
        for start in range(n):
            current_cost += abs(ord(s[start]) - ord(t[start]))
            while current_cost > maxCost:
                current_cost -= abs(ord(s[end]) - ord(t[end]))
                end += 1
            if maximum_window < start - end + 1:
                maximum_window = start - end + 1
        
        return maximum_window
