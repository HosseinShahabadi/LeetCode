class Solution:
    def maxProfitAssignment(self, difficulty: list[int], profit: list[int], worker: list[int]) -> int:
        dipo = [(i, j) for i, j in zip(difficulty, profit)]
        ans, j, best, k = 0, 0, 0, len(dipo)
        
        dipo.sort()
        worker.sort()
        
        for work in worker:
            while j < k and work >= dipo[j][0]:
                best = max(best, dipo[j][1])
                j += 1
            
            ans += best
        
        return ans
