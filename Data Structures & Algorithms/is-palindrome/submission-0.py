class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = "".join([c for c in s if c.isalnum()]).lower()
        print(cleaned_s)
        reversed_s = cleaned_s[::-1] 
        for i,c in enumerate(cleaned_s):
            if c != reversed_s[i]:
                return False
        return True