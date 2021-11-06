class Solution:
    def isValid(self, s: str) -> bool:        
        
        parenthese_table = {
            '(' : ')',
            '{' : '}',
            '[' : ']',
            ')' : '(',
            '}' : '{',
            ']' : '['            
        }        
        parenthese_open_list = ['(', '{', '[']
        parenthese_queue = []
        
        # O(n)
        for item in s:
            if item in parenthese_open_list:
                parenthese_queue.append(item)
            else:
                if len(parenthese_queue) == 0 or item != parenthese_table[parenthese_queue[-1]]:
                    return False
                else:
                    parenthese_queue.pop()
        
        if len(parenthese_queue) != 0:
            return False
        return True