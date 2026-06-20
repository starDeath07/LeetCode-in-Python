class Solution:
    def maxBuilding(self, n: int, restrictions: list[list[int]]) -> int:
        restrictions.append([1, 0])
        restrictions.append([n, n - 1])

        restrictions.sort(key=lambda x: x[0])

        m = len(restrictions)

        prev = restrictions[0]

        for i in range(1, m):
            curr = restrictions[i]
            distance = curr[0] - prev[0]
            curr[1] = min(curr[1], prev[1] + distance)
            prev = curr

        nxt = restrictions[-1]

        for i in range(m - 2, -1, -1):
            curr = restrictions[i]
            distance = nxt[0] - curr[0]
            curr[1] = min(curr[1], nxt[1] + distance)
            nxt = curr

        ans = 0

        prev = restrictions[0]

        for i in range(1, m):
            curr = restrictions[i]
            distance = curr[0] - prev[0]
            ans = max(ans, (prev[1] + curr[1] + distance) // 2)
            prev = curr

        return ans
