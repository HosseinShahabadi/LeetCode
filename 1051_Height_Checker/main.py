# Notice:
# I want to thank 'anwendeng' for their excellent solution.
# Their approach was more efficient than mine, so I have incorporated their answer into my code.
# All credit goes to anwendeng for this improvement. Much appreciated!
class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        freq = [0] * 101

        for x in heights:
            freq[x] += 1
        cnt = 0

        for x in range(1, 101):
            f = freq[x]
            for i in range(cnt, cnt + f):
                heights[i] -= x
            cnt += f
        
        return len(heights) - heights.count(0)

# My Solution.
class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        def qsort(inlist):
            if not inlist:
                return []
            else:
                pivot = inlist[0]
                lesser = qsort([x for x in inlist[1:] if x < pivot])
                greater = qsort([x for x in inlist[1:] if x >= pivot])
                return lesser + [pivot] + greater

        sorted_heights = qsort(heights)
        ans = 0
        n = len(heights)
        for i in range(n):
            if heights[i] != sorted_heights[i]:
                ans += 1
        
        return ans
