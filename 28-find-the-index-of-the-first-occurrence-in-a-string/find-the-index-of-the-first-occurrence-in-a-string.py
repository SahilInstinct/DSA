class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i,j = len(haystack),len(needle)

        for k in range(i - j + 1):
            if haystack[k:k+j] == needle:
                return k
        return -1