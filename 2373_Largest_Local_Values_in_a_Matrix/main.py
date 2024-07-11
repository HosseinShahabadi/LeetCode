class Solution:
    def largestLocal(self, grid: list[list[int]]) -> list[list[int]]:
        output = []
        x = range(len(grid) - 2)

        for i in x:
            listofmaximums = []
            for j in x:
                list = []
                for k in range(i, i + 3):
                    for l in range(j, j + 3):
                        list.append(grid[k][l])
                listofmaximums.append(max(list))

            output.append(listofmaximums)
        
        return output
