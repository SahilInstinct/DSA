class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        freq1 = {}
        freq2 = {}

        for char in word1:
            freq1[char] = freq1.get(char,0) + 1
        for char in word2:
            freq2[char] = freq2.get(char,0) + 1
        
        if set(freq1.keys()) != set(freq2.keys()):
            return False
        return sorted(freq1.values()) == sorted(freq2.values())
        

