class Solution:
    def getLucky(self, s: str, k: int) -> int:
        ord_of_a = ord('a')
        s = ''.join([str(ord(ch) - ord_of_a + 1) for ch in s])
        for _ in range(k):
            s = str(sum([int(num) for num in s]))
        
        return int(s)
