class Solution:
    def stoneGameIII(self, stoneValue: list[int]) -> str:
        n = len(stoneValue)
        dp: list[int] = [0] * (n + 1)

        for index in range(n - 1, -1, -1):
            score = -(10**10)
            tot = 0

            for i in range(index, min(index + 3, n)):
                tot += stoneValue[i]
                score = max(score, tot - dp[i + 1])

            dp[index] = score

        if dp[0] == 0:
            return "Tie"
        elif dp[0] < 0:
            return "Bob"

        return "Alice"
