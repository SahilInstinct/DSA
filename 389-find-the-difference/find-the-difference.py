class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hmap = {}
        for i in range(len(s)):
            hmap[s[i]] = hmap.get(s[i],0) + 1
        
        for char in t:
            if hmap.get(char,0) == 0:
                return char
            hmap[char] = hmap.get(char,0) - 1
        