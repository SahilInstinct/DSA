class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hmap = {}
        for i in s:
            hmap[i] = hmap.get(i,0) + 1
        
        for j in t:
            if hmap.get(j,0) == 0:
                return False
            hmap[j] = hmap[j] - 1
        return True