class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        s2t = {}
        t2s = {}

        for i in range(len(s)):
            a = s[i]
            b = t[i]

            if a in s2t and s2t[a] != b:
                return False
            
            if b in t2s and t2s[b] != a:
                return False
            
            s2t[a] = b
            t2s[b] = a
        
        return True
