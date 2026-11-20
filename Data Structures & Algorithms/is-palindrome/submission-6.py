class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) <= 1:  
            return True  
        text = " ".join(char.lower() for char in s if char.isalnum()) 
        l = 0 
        r = int(len(text)-1)
        while l < r and text[l] == text[r]: 
            l += 1
            r -= 1
        if l <= len(text)/2 and r <= len(text)/2: 
            return True 
        else: 
            return False 
        