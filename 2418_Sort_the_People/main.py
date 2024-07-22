class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        n = len(heights)
        name_height = []
        for i in range(n):
            name_height.append([heights[i], names[i]])
        name_height.sort(reverse=True)
        
        ans = []
        for row in name_height:
            ans.append(row[1])
        
        return ans
