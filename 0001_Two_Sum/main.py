class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        copynums = copy.deepcopy(nums)
        nums.sort()
        minimum_index = 0
        maximum_index = -1
        for i in range(len(nums)):
            value = (nums[minimum_index] + nums[maximum_index])
            if target == value:
                break
            elif target > value:
                minimum_index += 1
            else:
                maximum_index -= 1
        
        minimum_index = copynums.index(nums[minimum_index])
        maximum_index = copynums.index(nums[maximum_index])
        if minimum_index == maximum_index:
            for i in range(len(copynums)):
                if copynums[maximum_index] == copynums[i] and i != maximum_index:
                    maximum_index = i
                    break
        if minimum_index < maximum_index:
            return [minimum_index, maximum_index]
        else:
            return [maximum_index, minimum_index]