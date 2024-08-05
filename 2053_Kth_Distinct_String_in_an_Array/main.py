from collections import Counter


class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        counter = Counter(arr)
        for key, val in counter.items():
            if val == 1:
                k -= 1
            if not k:
                return key
        
        return ""
