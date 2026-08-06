class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        win_sum = 0
        res = float('inf')
        for i in range(len(nums)):
            win_sum += nums[i]
            while win_sum >= target:
                res = min(res, i - left + 1)
                win_sum -= nums[left]
                left += 1
        return 0 if res == float('inf') else res