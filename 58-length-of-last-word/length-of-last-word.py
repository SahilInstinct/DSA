class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1

        while i>= 0 and s[i] == ' ':
            i -= 1

        sol = 0
        while i>=0 and s[i] != ' ':
            sol += 1
            i -= 1

        return sol