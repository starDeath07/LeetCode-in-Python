class Solution:
    def minimumCost(
        self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int
    ) -> int:
        ans = cost1 * need1 + cost2 * need2
        mini = min(need1, need2)
        ans = min(
            ans,
            mini * costBoth
            + max(0, need1 - mini) * min(cost1, costBoth)
            + max(0, need2 - mini) * min(cost2, costBoth),
        )
        return ans
