from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        n = len(s)
        step = len(words[0])
        total_length = len(words) * step
        word_count = Counter(words)
        ans = []
        
        for i in range(step):
            left = i
            right = i
            current_count = Counter()
            
            while right + step <= n:
                word = s[right:right + step]
                right += step
                
                if word in word_count:
                    current_count[word] += 1
                    while current_count[word] > word_count[word]:
                        current_count[s[left:left + step]] -= 1
                        left += step
                    if right - left == total_length:
                        ans.append(left)
                else:
                    current_count.clear()
                    left = right
        
        return ans
