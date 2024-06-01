class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        result = ''
        for i in range(len(strs[0])):
            for string in strs[1:]:
                if i >= len(string) or string[i] != strs[0][i]:
                    return result
            result += strs[0][i]
        
        return result
