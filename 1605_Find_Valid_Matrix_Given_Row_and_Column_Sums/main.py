class Solution:
    def restoreMatrix(self, rowSum: list[int], colSum: list[int]) -> list[list[int]]:
        n, m = len(rowSum), len(colSum)
        ans = []
        for i in range(n):
            ans.append([0] * m)
        
        while sum(rowSum) or sum(colSum):
            rmin = float('inf')
            for i in range(n):
                if rowSum[i] and rmin > rowSum[i]:
                    rmin = rowSum[i]
                    rindex = i

            cmin = float('inf')
            for i in range(m):
                if  colSum[i] and cmin > colSum[i]:
                    cmin = colSum[i]
                    cindex = i

            if cmin < rmin:
                ans[rindex][cindex] = cmin
                rowSum[rindex] -= cmin
                colSum[cindex] -= cmin
            else:
                ans[rindex][cindex] = rmin
                rowSum[rindex] -= rmin
                colSum[cindex] -= rmin

        return ans
