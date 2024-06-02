class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        # Special thanks to hi-malik for their valuable solution. 
        # I initially had an O(n^2) solution that worked perfectly, but their approach 
        # improved the time complexity to O(n).
        n = len(gas)
        total_surplus, surplus, start = 0, 0, 0
        
        for i in range(n):
            total_surplus += gas[i] - cost[i]
            surplus += gas[i] - cost[i]
            if surplus < 0:
                surplus = 0
                start = i + 1
        
        if total_surplus >= 0:
            return start
        return -1
    