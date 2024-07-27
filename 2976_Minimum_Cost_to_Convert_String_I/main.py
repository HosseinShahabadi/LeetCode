class Solution:
    def minimumCost(self, source: str, target: str, original: list[str], changed: list[str], cost: list[int]) -> int:
        dist = [[float('inf')] * 26 for _ in range(26)]

        for i in range(26):
            dist[i][i] = 0
        
        for org, chg, cst in zip(original, changed, cost):
            org_char = ord(org) - ord("a")
            chg_char = ord(chg) - ord("a")
            dist[org_char][chg_char] = min(dist[org_char][chg_char], cst)
        
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        ans = 0
        for s, t in zip(source, target):
            if s != t:
                x = ord(s) - ord('a')
                y = ord(t) - ord('a')
                if dist[x][y] == float('inf'):
                    return -1
                ans += dist[x][y]
        
        return ans
