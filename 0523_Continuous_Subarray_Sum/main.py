class Solution(object):
    def checkSubarraySum(self, nums, k):
        # Notice:
        # A big thanks to decoder2025 for providing this solution.
        # Your code helped me understand the problem and find the solution efficiently.
        # Much appreciated!
        
        map = {0: -1}
        sum = 0

        for i in range(len(nums)):
            sum += nums[i]
            rem = sum % k

            if rem in map:
                if i - map[rem] > 1:
                    return True
            else:
                map[rem] = i

        return False
