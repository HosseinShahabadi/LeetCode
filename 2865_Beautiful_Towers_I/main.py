class Solution:
    def sum_of_heights(self, heights, index):
        modified_heights = []
        peak = heights[index]
        
        up_peak = peak
        down_peak = peak
        
        for i in range(index - 1, -1, -1):
            if heights[i] < up_peak:
                up_peak = heights[i]
            modified_heights.append(up_peak)

        modified_heights.append(peak)

        for i in range(index + 1, len(heights)):
            if heights[i] < down_peak:
                down_peak = heights[i]
            modified_heights.append(down_peak)
        
        output = 0
        for i in range(len(modified_heights)):
            output += modified_heights[i]
        
        return output

    def maximumSumOfHeights(self, heights: List[int]) -> int:
        mountaintops = []
        mountaintops.append(0)
        mountaintops.append(len(heights) - 1)
        for i in range(1, len(heights) - 1):
            if heights[i] <= heights[i + 1]:
                continue
            elif heights[i] < heights[i - 1]:
                continue
            else:
                mountaintops.append(i)
         
        max = 0
        for i in range(len(mountaintops)):
            index = mountaintops[i]
            value = self.sum_of_heights(heights, index)
            if max < value:
                max = value
        
        return max
