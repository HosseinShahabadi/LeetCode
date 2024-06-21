# Used editorial for optimization.
class Solution:
    def maxSatisfied(self, customers: list[int], grumpy: list[int], minutes: int) -> int:
        n = len(customers)
        
        curwin = 0
        for i in range(minutes):
            curwin += customers[i] * grumpy[i]

        maxwin = curwin
        for i in range(minutes, n):
            curwin += (customers[i] * grumpy[i]) - (customers[i - minutes] * grumpy[i - minutes])
            maxwin = max(maxwin, curwin)

        return maxwin + sum(customers[i] for i in range(n) if not grumpy[i])
