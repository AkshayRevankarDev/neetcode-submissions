class Solution:
    def isPalindrome(self, s: str) -> bool:
        newString = ""
        for h in s:
            if h.isalnum():
                newString += h.lower()
        return newString == newString[::-1]