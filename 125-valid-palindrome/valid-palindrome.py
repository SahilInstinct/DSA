class Solution:
    def isPalindrome(self, s: str) -> bool:
        txt = ''.join(char for char in s if char.isalnum()).lower()

        i = 0
        j = len(txt) - 1
        while i < j:
            if txt[i] != txt[j]:
                return False
            i += 1
            j -= 1
        return True