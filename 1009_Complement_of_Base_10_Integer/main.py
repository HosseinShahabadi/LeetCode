class Solution:
    def bitwiseComplement(self, n: int) -> int:
        return int(''.join(['0' if char == '1' else '1' for char in format(n, 'b')]), 2)
        