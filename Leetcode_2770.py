class Solution:
    def maximumJumps(self, nums: list[int], target: int) -> int:
        n = len(nums)
        dp = [0] * n

        for i in range(n - 2, -1, -1):
            ans = -(10**10)
            for j in range(i + 1, n):
                diff = nums[j] - nums[i]
                if diff >= -target and diff <= target:
                    ans = max(ans, 1 + dp[j])
            dp[i] = ans

        return -1 if dp[0] < 0 else dp[0]
