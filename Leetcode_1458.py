from typing import List


class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: list[int]) -> int:
        m, n = len(nums1), len(nums2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        neg_inf = -((10**9) + 7)
        dp[m] = [neg_inf] * (n + 1)

        for i in range(m + 1):
            dp[i][n] = neg_inf

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                take = nums1[i] * nums2[j] + max(0, dp[i + 1][j + 1])
                skip = max(dp[i + 1][j], dp[i][j + 1])
                dp[i][j] = max(take, skip)

        return dp[0][0]
