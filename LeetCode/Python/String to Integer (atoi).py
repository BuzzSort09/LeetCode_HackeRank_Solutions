class Solution:
    def myAtoi(self, s: str) -> int:
        
        # time complexity: O(n)
        
        sign = 1   
        number_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        output = 0
        MAX_INIT = 2 ** 31 -1
        MIN_INIT = -2 ** 31

        # find sign and remove whitespace
        index = 0
        
        # remove whitespace
        while index < len(s) and s[index] == ' ':
            index += 1
        
        # check '-' or '+'
        if index < len(s) and s[index] == '-':
            index += 1
            sign = -1
        elif index < len(s) and s[index] == '+':
            index += 1
            
        # check number from 0 to 9
        while index < len(s) and s[index] in number_list:
            output = output * 10 + int(s[index])
            index += 1
            
        output = output * sign     
        if output < 0:
            return max(output, MIN_INIT)
        else:
            return min(output, MAX_INIT)

