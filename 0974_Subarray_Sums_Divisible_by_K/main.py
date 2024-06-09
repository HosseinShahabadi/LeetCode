class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        ans = 0
        sum = 0
        memo = {0: 1}
        
        for num in nums:
            sum += num
            mod = sum % k
            if mod in memo:
                ans += memo[mod]
                memo[mod] += 1
            else:
                memo[mod] = 1
        
        return ans
