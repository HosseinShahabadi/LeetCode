class Solution:
    def calculate(self, s: str) -> int:
        def calculateNum(s: str) -> int:
            n = len(s)
            neg = False
            nums = []
            num = 0
            
            global i
            while i < n:
                char = s[i]
                i += 1

                # Detect numbers.
                if char.isdigit():
                    num = num*10 + int(char)
                
                # Detect operands.
                # -----------------------------------------
                elif char == '+':
                    nums.append(-num) if neg else nums.append(num)
                    neg = False
                    num = 0
                
                # -----------------------------------------
                elif char == '-':
                    nums.append(-num) if neg else nums.append(num)
                    neg = True
                    num = 0
                
                # -----------------------------------------
                elif char == '(':
                    num = calculateNum(s)
                    nums.append(-num) if neg else nums.append(num)
                    neg = False
                    num = 0
                
                # -----------------------------------------
                elif char == ')':
                    return sum(nums) - num if neg else sum(nums) + num

            return sum(nums) - num if neg else sum(nums) + num
        
        global i
        i = 0
        return calculateNum(s)
