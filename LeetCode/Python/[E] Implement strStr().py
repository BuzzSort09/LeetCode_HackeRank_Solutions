class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
                
        needle_length = len(needle)
        index = 0
        
        # O(n)
        while index <= len(haystack):
            if needle == haystack[index:index+needle_length]:
                return index
            else:
                index += 1
                
        return -1