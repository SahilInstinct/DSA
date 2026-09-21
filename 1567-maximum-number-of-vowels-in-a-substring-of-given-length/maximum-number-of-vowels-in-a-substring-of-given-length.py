class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        res = sum(1 for char in s[:k] if char in vowels)
        max_count = res

        for i in range(k,len(s)):
            if s[i] in vowels:
                res += 1
            if s[i - k] in vowels:
                res -= 1
            max_count = max(max_count,res)
        
        return max_count
