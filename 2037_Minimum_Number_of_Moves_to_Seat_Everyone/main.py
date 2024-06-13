class Solution:
    def minMovesToSeat(self, seats, students):
        pos = [0] * 101
        n = len(seats)
        for i in range(n):
            pos[seats[i]] += 1
            pos[students[i]] -= 1
        
        ans = 0
        current = 0
        for i in pos:
            ans += abs(current)
            current += i
        return ans
