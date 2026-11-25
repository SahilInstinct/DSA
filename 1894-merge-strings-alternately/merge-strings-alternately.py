class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        p,q = 0,0

        while p != len(word1) and q != len(word2):
            res += word1[p]
            res += word2[q]
            p += 1
            q += 1
        
        res += word1[p:]
        res += word2[q:]

        return res