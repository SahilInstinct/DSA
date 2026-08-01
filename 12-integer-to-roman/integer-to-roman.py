class Solution:
    def intToRoman(self, num: int) -> str:
        values = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        roms = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']

        sol = ""

        for i in range(len(values)):
            while num >= values[i]:
                sol += roms[i]
                num -= values[i]
        return sol
