class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        def findSubsetsXOR(nums, n) -> list[list[int]]:
            sum = 0

            '''Thanks to GeeksforGeeks'''
            # Loop through all possible subsets using bit manipulation
            for i in range(1, 1 << n):
                # Loop through all elements of the input array
                new_list = []
                for j in range(n):
                    #Check if the jth bit is set in the current subset
                    if (i & (1 << j)) != 0:
                        #If the jth bit is set, add the jth element to the subset
                        new_list.append(nums[j])
                sum += listXOR(new_list)
            return sum

        def listXOR(newnums: list[int]) -> int:
            output = newnums[0]
            for num in newnums[1:]:
                output ^= num
            return output
        
        return findSubsetsXOR(nums, len(nums))
