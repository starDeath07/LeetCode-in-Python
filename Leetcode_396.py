class Solution:
    def maxRotateFunction(self, nums: list[int]) -> int:
        n = len(nums)
        ans = -(10**10)
        total, best = 0, 0

        for i in range(n):
            total += nums[i]
            best += i * nums[i]

        ans = max(ans, best)

        for i in range(1, n):
            best += total - n * nums[n - i]
            ans = max(ans, best)

        return ans
