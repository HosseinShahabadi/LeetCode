class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        memo = {}
        n1, n2 = len(arr1), len(arr2)

        for i in range(n2):
            memo[arr2[i]] = {'position': i, 'count': 0}

        residue = []
        for i in range(n1):
            num = arr1[i]
            if num in memo:
                memo[num]['count'] += 1
            else:
                residue.append(num)
        
        arr1 = []
        for k, v in memo.items():
            arr1.extend([k] * v['count'])
        
        residue.sort()
        arr1.extend(residue)
        return arr1
