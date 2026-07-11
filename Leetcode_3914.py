class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(1, n):
            if nums[i - 1] > nums[i]:
                ans += nums[i - 1] - nums[i]

        return ans
