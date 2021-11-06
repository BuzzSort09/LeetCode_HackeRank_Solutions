class Solution:
    def reverse(self, x: int) -> int:
        
        MAX_INIT = 2**31 -1
        MIN_INIT = -2 ** 31
        
        value = '0'
        sign = 1
        
        if x < 0:
            sign = -1
            x = x * -1
       
        # O(n)
        while x != 0:            
            one_digit = x % 10 
            x = x // 10       
            value += str(one_digit)
         
        int_value = int(value) * sign        
        if int_value < MIN_INIT or int_value > MAX_INIT:
            return 0
        
        return int_value