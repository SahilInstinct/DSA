class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        alt = 0
        max_alt = 0
        for i in range(len(gain)):
            alt += gain[i]
            max_alt = max(max_alt,alt)
        return max_alt