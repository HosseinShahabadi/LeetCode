class Solution:
    def survivedRobotsHealths(self, positions: list[int], healths: list[int], directions: str) -> list[int]:
        n = len(directions)
        robots = [[positions[i], directions[i], healths[i], i] for i in range(n)]
        robots.sort()

        stack = []

        for pos, dir, health, idx in robots:
            if dir == 'R':
                stack.append([pos, dir, health, idx])
            else:
                while stack and stack[-1][1] == 'R':
                    r_pos, r_dir, r_health, r_idx = stack.pop()
                    if r_health > health:
                        r_health -= 1
                        health = 0
                        stack.append([r_pos, r_dir, r_health, r_idx])
                        break
                    elif r_health < health:
                        health -= 1
                    else:
                        health = 0
                        break
                if health > 0:
                    stack.append([pos, dir, health, idx])

        stack.sort(key=lambda x: x[3])
        return [robot[2] for robot in stack]
