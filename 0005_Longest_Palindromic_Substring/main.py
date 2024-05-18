class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 1:
            return s
        
        maxPalindromeLength = 1
        maxPalindromeString = s[0]

        for i in range(n-1):
            palindromeString = self.isPalindrome(s, i)

            if len(palindromeString) > len(maxPalindromeString):
                maxPalindromeString = palindromeString
        
        return maxPalindromeString
    

    def isPalindrome(self, s: str, index: int) -> str:
        left = index
        right = index
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        odd = s[left + 1:right]

        left = index
        right = index + 1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        even = s[left + 1:right]

        if len(even) > len(odd):
            return even
        else:
            return odd
