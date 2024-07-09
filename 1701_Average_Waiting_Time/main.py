class Solution:
    def averageWaitingTime(self, customers: list[list[int]]) -> float:
        wait = customers[0][1]
        base = customers[0][0] + wait
        n = len(customers)

        for (i, j) in customers[1:]:
            if base > i:
                wait += (base - i + j)
                base += j
            else:
                wait += j
                base = i + j

        return wait / n
