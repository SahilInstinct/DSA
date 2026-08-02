class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows > len(s):
            return s
        
        rows = [""] * numRows
        rowcount = 0
        goingdown = False

        for ch in s:
            rows[rowcount] = rows[rowcount] + ch

            if rowcount == 0 or rowcount == numRows - 1:
                goingdown = not goingdown
            
            if goingdown == True:
                rowcount += 1
            else:
                rowcount -= 1
        return "".join(rows)