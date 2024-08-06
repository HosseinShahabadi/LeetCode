from collections import Counter


class Solution:
    def minimumPushes(self, word: str) -> int:
        ans = 0
        counter = [[val, key] for key, val in Counter(word).items()]
        counter.sort(reverse=True)
        
        for index, [val, key] in enumerate(counter):
            if index <= 7:
                ans += val
            elif index <= 15:
                ans += val * 2
            elif index <= 23:
                ans += val * 3
            else:
                ans += val * 4

        return ans
