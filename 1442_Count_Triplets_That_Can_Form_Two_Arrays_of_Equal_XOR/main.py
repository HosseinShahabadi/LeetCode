class Solution:
    def countTriplets(self, arr: list[int]) -> int:
        # Special thanks to hi-malik for their valuable solution, which greatly helped in improving this code.
        count = 0
        
        for i in range(len(arr)):
            val = arr[i]
            
            for k in range(i + 1, len(arr)):
                val ^= arr[k]
                
                if val == 0:
                    count += (k - i)
        
        return count
    