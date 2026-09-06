from functools import cache


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)

        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][m] = 1

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                take, skip = 0, 0
                if s[i] == t[j]:
                    take = dp[i + 1][j + 1]
                skip = dp[i + 1][j]

                dp[i][j] = take + skip

        return dp[0][0]

    # this is the recursive version of the code

    def numDistinct(self, s: str, t: str) -> int:
        @cache
        def finder(s: str, t: str, i: int, j: int) -> int:
            if j == len(t):
                return 1
            if i == len(s):
                return 0

            take, skip = 0, 0

            if s[i] == t[j]:
                take = finder(s, t, i + 1, j + 1)
            skip = finder(s, t, i + 1, j)

            return take + skip
