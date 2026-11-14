import string

class Solution:
    # well it seems easy but after checking the solution its anything but
    # we have to use left and right pointers
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.isAlphaNum(s[l]):
                l += 1
            while r > l and not self.isAlphaNum(s[r]):
                r -= 1
            if s[l].lower() == s[r].lower():
                l, r = l + 1, r - 1
            else: return False
        return True
    
    def isAlphaNum(self, c):
        return ((ord('A') <= ord(c) <= ord('Z')) or (ord('0') <= ord(c) <= ord('9')) or (ord('a') <= ord(c) <= ord('z')))
        