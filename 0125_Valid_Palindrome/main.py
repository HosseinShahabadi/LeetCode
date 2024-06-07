class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(s.lower().split())
        new_s = ''
        for char in s:
            if 0 <= ord(char) - ord('a') < 26 or char.isdigit():
                new_s += char

        n = len(new_s)
        # Odd ----------
        if n % 2:
            if new_s[:int((n-1)/2)] == new_s[int((n+1)/2):][::-1]:
                return True
            else:
                return False
        # Even ---------
        else:
            if new_s[:int(n/2)] == new_s[int(n/2):][::-1]:
                return True
            else:
                return False
