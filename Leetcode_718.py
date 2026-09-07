class Solution:
    def findLength(self, nums1: list[int], nums2: list[int]) -> int:
        n = len(nums1)
        m = len(nums2)

        dp: list[list[int]] = [[-1] * (m + 1) for _ in range(n + 1)]
        ans = 0

        def finder(x: int, y: int) -> int:
            if x >= n or y >= m:
                return 0

            if dp[x][y] != -1:
                return dp[x][y]

            if nums1[x] == nums2[y]:
                dp[x][y] = 1 + finder(x + 1, y + 1)
            else:
                dp[x][y] = 0
            return dp[x][y]

        for i in range(n):
            for j in range(m):
                ans = max(ans, finder(i, j))

        return ans
