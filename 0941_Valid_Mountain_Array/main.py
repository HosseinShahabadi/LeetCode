class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        if len(arr) < 3:
            return False
        
        maxnum_index = 0
        up_rising = True
        for i in range(len(arr) - 1):
            if arr[maxnum_index] < arr[i]:
                maxnum_index = i

            if arr[i] == arr[i+1]:
                return False
            if up_rising:
                if arr[i] < arr[i+1]:
                    continue
                else:
                    up_rising = False
            else:
                if arr[i] > arr[i+1]:
                    continue
                else:
                    return False
        
        if maxnum_index == 0 or maxnum_index == (len(arr) - 1):
            return False
        return not up_rising
