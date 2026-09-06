class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum = 0
        result = float('inf')
        left = 0
        for j in range(len(nums)):
            sum += nums[j]
            while sum >= target:
                result = min(result, j - left + 1)
                sum -= nums[left]
                left += 1

        return 0 if result == float("inf") else result
            
                 