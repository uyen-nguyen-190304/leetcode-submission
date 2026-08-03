class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Standardize the input string
        s = "".join(char.lower() for char in s if char.isalnum())
        
        # Standard two pointers check
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True