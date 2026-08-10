class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp: list[bool] = [False] * (n + 1)

        for i in range(1, n + 1):
            for j in range(1, int(i**0.5) + 1):
                if not dp[i - j * j]:
                    dp[i] = True

        return dp[n]
