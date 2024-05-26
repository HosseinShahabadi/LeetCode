class Solution:
    def canJump(self, nums: list[int]) -> bool:
        # Notice:
        # Initially, I implemented the solution using recursion with memoization.
        # While this approach worked correctly, it was not fast enough for larger inputs.
        # To improve performance, I found a very creative and efficient solution by "frestre".
        # I have added their solution under their own name to this folder, which significantly
        # enhances the performance for large inputs.
        
        gas = 0
        for n in nums:
            if gas < 0:
                return False
            elif n > gas:
                gas = n
            gas -= 1
            
        return True
