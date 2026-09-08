class Solution:
    def jump(self, nums: List[int]) -> int:
        farthest = 0
        curr_end = 0
        jump = 0
        for i in range(len(nums)-1):
            farthest = max(farthest, i + nums[i])
            if curr_end == i:
                jump += 1
                curr_end = farthest
        return jump

