class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0

        is_negative = False
        if s[0] == '-':
            s = s[1:]
            is_negative = True
        elif s[0] == '+':
            s = s[1:]
        if not s:
            return 0
    
        if not s[0].isdigit():
            return 0
        
        num = 0
        try:
            num = int(s)
        except:
            num_string = '0'
            for i in range(len(s)):
                if s[i].isdigit():
                    num_string += s[i]
                else:
                    break
            num = int(num_string)

        if not is_negative:
            if num > 2**31 - 1:
                return 2**31 - 1
            return num
        else:
            if - num < - 2**31:
                return - 2**31
            return num * -1
