class Solution:
    def romanToInt(self, s: str) -> int:
        n = len(s)
        nums = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        result = nums[s[-1]]
        power = 0
        for i in range(n-1):
            power += nums[s[i]]
            if nums[s[i]] == nums[s[i+1]]:
                continue
            
            if nums[s[i]] > nums[s[i+1]]:
                result += power
            else:
                result -= power

            power = 0
        
        result += power
        return result
