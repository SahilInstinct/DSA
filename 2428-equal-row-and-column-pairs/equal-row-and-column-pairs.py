class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        freq = {}
        res = 0
        for i in grid:
            i = tuple(i)
            freq[i] = freq.get(i,0)+1
        
        for i in range(len(grid)):
            col = tuple(grid[j][i] for j in range(len(grid)))

            if col in freq:
                res += freq[col]
        return res

                