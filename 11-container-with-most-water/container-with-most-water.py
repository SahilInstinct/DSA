class Solution:
    def maxArea(self, height: List[int]) -> int:
        i,j = 0, len(height) -1
        max_wat = 0
        while i < j:
            wdth = j - i
            max_wat = max(wdth * min(height[i],height[j]),max_wat)
            if height[i] < height[j] :
                i += 1
            else:
                j -= 1
        return max_wat