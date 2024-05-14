class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        stringLength = len(s)
        if stringLength <= 1:
            return stringLength
        
        start_idx = 0
        last_idx = {}
        maximum = 0

        for i in range(0, stringLength):
            if s[i] in last_idx:
                start_idx = max(start_idx, last_idx[s[i]] + 1)
            
            maximum = max(maximum, i-start_idx + 1)
            last_idx[s[i]] = i

        return maximum