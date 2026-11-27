class Solution:
    def maximumSaleItems(self, items: list[list[int]], budget: int) -> int:
        n = len(items)
        dp: list[int] = [0] * (budget + 1)
        freq: list[int] = [0] * n
        ans = 0
        mini = 10**10

        for i in range(n - 1, -1, -1):
            mini = min(mini, items[i][1])

            for j in range(n):
                if items[j][0] % items[i][0] == 0:
                    freq[i] += 1

            for j in range(budget, 0, -1):
                skip = dp[j]
                take = 0

                if j >= items[i][1]:
                    take = freq[i] + dp[j - items[i][1]]
                dp[j] = max(take, skip)

        ans = 0

        for i in range(budget + 1):
            remaining = budget - i
            ans = max(ans, dp[i] + remaining // mini)

        return ans
