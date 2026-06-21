class Solution:
    def maxIceCream(self, costs: list[int], coins: int) -> int:
        costs.sort()
        n = len(costs)
        for i in range(n):
            coins -= costs[i]
            if coins < 0:
                return i
        return n
