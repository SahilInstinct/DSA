class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        p = 0
        q = 0
        while p < len(word1) and q < len(word2):
            res.append(word1[p])
            res.append(word2[q])
            p += 1
            q += 1
        
        while p < len(word1):
            res.append(word1[p])
            p += 1
        
        while q < len(word2):
            res.append(word2[q])
            q += 1
        
        return "".join(res)