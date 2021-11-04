class Solution:
    def longestPalindrome(self, s: str) -> str:

        # 0(2N) --> 0(N)
        def helper(left, right):
            while (left >=0 and right < len(s) and s[left] == s[right]):
                left = left - 1
                right = right + 1
            return s[left+1:right]
        
        palindrome = ""
        for index in range(len(s)):
            sample = helper(index, index)
            if len(palindrome) < len(sample):
                palindrome = sample
                
            sample = helper(index, index+1)
            if len(palindrome) < len(sample):
                palindrome = sample
        
        return palindrome
        