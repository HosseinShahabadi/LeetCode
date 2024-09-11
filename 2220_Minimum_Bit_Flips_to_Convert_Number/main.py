class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        start_b = "{0:b}".format(start)
        goal_b = "{0:b}".format(goal)
        lenstart_b = len(start_b)
        lengoal_b = len(goal_b)

        if lenstart_b >= lengoal_b:
            x = lenstart_b - lengoal_b
            ans = sum([1 for i in range(x) if start_b[i] == '1'])
            for i in range(x, lenstart_b):
                if start_b[i] != goal_b[i - x]:
                    ans += 1
        else:
            x = lengoal_b - lenstart_b
            ans = sum([1 for i in range(x) if goal_b[i] == '1'])
            for i in range(x, lengoal_b):
                if start_b[i - x] != goal_b[i]:
                    ans += 1
        
        return ans
