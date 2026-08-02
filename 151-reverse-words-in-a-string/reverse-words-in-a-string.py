class Solution:
    def reverseWords(self, s: str) -> str:
        lis = s.split()
        left = 0
        right = len(lis) - 1
        while left < right:
            lis[left],lis[right] = lis[right],lis[left]
            left += 1
            right -= 1
        return " ".join(lis)