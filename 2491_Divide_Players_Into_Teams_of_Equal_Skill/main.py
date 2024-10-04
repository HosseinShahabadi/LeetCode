class Solution:
    def dividePlayers(self, skill: list[int]) -> int:
        skill.sort()
        ans = 0
        base = skill[0] + skill[-1]
        for i in range(int(len(skill)/2)):
            x, y = skill[i], skill[-(i + 1)]
            if x + y != base:
                return -1
            else:
                ans += (x * y)
        
        return ans
