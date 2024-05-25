class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        word_set = set(wordDict)  # Use a set for faster lookup
        memo = {}  # Dictionary to store memoized results
        
        def backtrack(start: int) -> list[str]:
            if start in memo:
                return memo[start]
            
            results = []
            if start == len(s):
                return [""]
            
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in word_set:
                    sub_results = backtrack(end)
                    for sub_result in sub_results:
                        if sub_result:
                            results.append(word + " " + sub_result)
                        else:
                            results.append(word)
            
            memo[start] = results
            return results
        
        return backtrack(0)
