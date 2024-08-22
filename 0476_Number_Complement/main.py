class Solution:
    def findComplement(self, num: int) -> int:
        return int(''.join(['0' if char == '1' else '1' for char in format(num, 'b')]), 2)
