class Solution:
    def minOperations(self, logs: list[str]) -> int:
        ans = 0

        for log in logs:
            if log == './':
                continue
            elif log == '../':
                if ans:
                    ans -= 1
            else:
                ans += 1

        return ans
