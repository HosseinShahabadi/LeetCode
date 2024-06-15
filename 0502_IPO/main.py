class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        if max(capital) < w:
            if len(capital) < k:
                return w + sum(profits)
            else:
                profits.sort(reverse=True)
                return w + sum(profits[:k])

        for _ in range(k, 0, -1):
            index = None
            for i in range(len(capital)):
                if capital[i] <= w:
                    if index == None or profits[i] > profits[index]:
                        index = i
            
            if index == None:
                return w
            
            w += profits[index]
            capital.pop(index)
            profits.pop(index)

        return w
