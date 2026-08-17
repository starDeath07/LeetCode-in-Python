class Solution:
    def stoneGameV(self, stoneValue: list[int]) -> int:
        n = len(stoneValue)

        # Prefix sum
        prefix: list[int] = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        # dp[left][right] = maximum score
        dp: list[list[int]] = [[-1] * (n + 1) for _ in range(n + 1)]

        return self.finder(1, n, prefix, dp)

    def finder(
        self, left: int, right: int, prefix: list[int], dp: list[list[int]]
    ) -> int:
        if left >= right:
            return 0

        if dp[left][right] != -1:
            return dp[left][right]

        ans = 0

        # Try every possible split
        for i in range(left, right):
            # Sum of stoneValue[left ... i]
            left_sum = prefix[i] - prefix[left - 1]

            # Sum of stoneValue[i+1 ... right]
            right_sum = prefix[right] - prefix[i]

            if left_sum < right_sum:
                ans = max(ans, left_sum + self.finder(left, i, prefix, dp))

            elif right_sum < left_sum:
                ans = max(ans, right_sum + self.finder(i + 1, right, prefix, dp))

            else:
                ans = max(
                    ans,
                    left_sum
                    + max(
                        self.finder(left, i, prefix, dp),
                        self.finder(i + 1, right, prefix, dp),
                    ),
                )

        dp[left][right] = ans
        return ans
