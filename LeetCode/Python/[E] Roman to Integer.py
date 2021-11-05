class Solution:
    def romanToInt(self, s: str) -> int:

        roman_to_integer_table = {
            'CM': 900,
            'M': 1000,
            'CD': 400,
            'D': 500,            
            'XC': 90,
            'C': 100,
            'XL': 40,
            'L': 50,
            'IX': 9,
            'X': 10,
            'IV': 4,
            'V': 5,
            'I': 1
        }
        
        integer_output = 0
        index = 0
        while index < len(s):
            if len(s[index:index+2]) >= 2 and s[index:index+2] in roman_to_integer_table:
                integer_output = integer_output + roman_to_integer_table[s[index:index+2]]
                index += 1
            else:
                integer_output = integer_output + roman_to_integer_table[s[index]]
            index += 1

        return integer_output
