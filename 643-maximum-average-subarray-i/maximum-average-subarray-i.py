class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        sub_sum = sum(nums[:k])
        max_sum = sub_sum

        for i in range(k,len(nums)):
            sub_sum += nums[i]
            sub_sum -= nums[i-k]
            max_sum = max(max_sum,sub_sum)

        return max_sum/k