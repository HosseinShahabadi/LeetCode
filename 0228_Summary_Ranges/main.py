class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if not nums:
            return []
        
        n = len(nums)
        ans = []
        left = nums[0]
        right = nums[0]
        for i in range(1, n):
            num = nums[i]
            if num - 1 == nums[i-1]:
                right += 1
            else:
                if left != right:
                    ans.append(f'{left}->{right}')
                else:
                    ans.append(f'{left}')
                left = num
                right = num

        if left != right:
            ans.append(f'{left}->{right}')
        else:
            ans.append(f'{left}')

        return ans
