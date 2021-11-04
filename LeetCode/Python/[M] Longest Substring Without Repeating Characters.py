class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
                
#         # O (N^2)
#         longest_substring_count = 0
#         temp = []
        
#         if len(s) == 1:
#             return 1
        
#         for i in range(0, len(s)):
#             for j in range(i, len(s)):
#                 if s[j] not in temp:
#                     temp.append(s[j])
#                 else:
#                     if longest_substring_count <= len(temp):
#                         longest_substring_count = len(temp)
#                     temp = []
#                     break
                    
#         return longest_substring_count

            # O(N)
            string_queue = []
            longest_substring_count = 0
    
            if len(s) == 1:
                return 1
            
            for i in range(len(s)):
                if s[i] not in string_queue:
                    string_queue.append(s[i])
                else:
                    index = string_queue.index(s[i])
                    string_queue = string_queue[index+1:]
                    string_queue.append(s[i])
                    
                longest_substring_count = max(longest_substring_count, len(string_queue)) 
                
            return longest_substring_count    