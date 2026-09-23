class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        hmap = {}
        for nums in arr:
            hmap[nums] = hmap.get(nums,0) + 1
        
        return len(hmap.values()) == len(set(hmap.values()))