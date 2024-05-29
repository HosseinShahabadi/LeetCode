class Solution:
    def numSteps(self, s: str) -> int:
        def bin_add(*bin_nums: str) -> str: 
            return bin(sum(int(x, 2) for x in bin_nums))[2:]
        
        charge = 0
        while len(s) > 1:
            if s[-1] == '1':
                s = bin_add('1', s)[:-1]
                charge += 2
            else:
                s = s[:-1]
                charge += 1
        
        return charge
