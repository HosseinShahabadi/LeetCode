class Solution:
    def jump(self, nums: list[int]) -> int:
        # Notice:
        # Initially, I had an answer for this problem with O(n^2) time complexity, which worked perfectly.
        # However, I found a much more efficient O(n) time complexity solution by "N7_BLACKHAT".
        # I have integrated their solution into this code with full credits to them for their optimization.
        
        ans = 0
        end = 0
        jumps = 0

        for i in range(len(nums) - 1):
            jumps = max(jumps, i + nums[i])
            if jumps >= len(nums) - 1:
                ans += 1
                break
            if i == end:
                ans += 1
                end = jumps

        return ans
