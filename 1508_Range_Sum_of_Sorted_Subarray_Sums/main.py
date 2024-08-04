class Solution:
    def rangeSum(self, nums: list[int], n: int, left: int, right: int) -> int:
        ans = []
        for i in range(n):
            num = 0
            for j in range(i, n):
                num += nums[j]
                ans.append(num)
        
        ans.sort()
        return sum(ans[left-1:right]) % (10**9 + 7)
