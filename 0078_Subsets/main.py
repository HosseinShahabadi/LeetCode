class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
            n = len(nums)
            output = [[]]
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
                output.append(new_list)
            return output
        