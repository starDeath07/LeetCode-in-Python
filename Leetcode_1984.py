class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:
        n = len(nums)
        ans = 10**10
        nums.sort()
        for i in range(k - 1, n):
            ans = min(ans, nums[i] - nums[i - k + 1])
        return ans
