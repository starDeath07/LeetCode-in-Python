class Solution:
    def minimumCost(self, cost: list[int]) -> int:
        cost.sort()
        n = len(cost)
        ans = 0
        curr = 0

        for i in range(n - 1, -1, -1):
            curr += 1
            if curr % 3 == 0:
                continue
            ans += cost[i]
        return ans
