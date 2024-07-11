class Solution:
    def reverseParentheses(self, s: str) -> str:
        def reverseSTR(left: int, right: int) -> str:
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        

        parentheses = []
        n = len(s)
        for i in range(n):
            if s[i] == '(':
                parentheses.append([i, 0])
            elif s[i] == ')':
                for w in range(len(parentheses) - 1, -1, -1):
                    if parentheses[w][1] == 0:
                        parentheses[w][1] = i
                        break

        s = list(s)
        for i in range(len(parentheses)-1, -1, -1):
            reverseSTR(parentheses[i][0] + 1, parentheses[i][1] - 1)
        
        ans = ''
        for char in s:
            if char == '(' or char == ')':
                continue
            ans += char

        return ans
