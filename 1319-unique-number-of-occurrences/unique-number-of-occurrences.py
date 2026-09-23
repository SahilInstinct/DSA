class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        hmap = {}
        for nums in arr:
            hmap[nums] = hmap.get(nums,0) + 1
        occ = set()
        for (i, freq) in hmap.items():
            if freq in occ:
                return False
            occ.add(freq)
        return True