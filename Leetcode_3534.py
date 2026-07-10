class Solution:
    def pathExistenceQueries(
        self, n: int, nums: list[int], maxDiff: int, queries: list[list[int]]
    ) -> list[int]:
        LOG = n.bit_length() + 1
        nums_with_index: list[tuple[int, int]] = []
        ans: list[int] = []

        for index, value in enumerate(nums):
            nums_with_index.append((value, index))

        nums_with_index.sort()
        lookup = [0] * n

        for i in range(n):
            lookup[nums_with_index[i][1]] = i

        up: list[list[int]] = [[0] * LOG for _ in range(n)]

        j = 0
        for i in range(n):
            while (
                j + 1 < n
                and nums_with_index[j + 1][0] - nums_with_index[i][0] <= maxDiff
            ):
                j += 1
            up[i][0] = j

        for i in range(1, LOG):
            for j in range(n):
                up[j][i] = up[up[j][i - 1]][i - 1]

        for u, v in queries:
            nu = lookup[u]
            nv = lookup[v]

            if nu == nv:
                ans.append(0)
                continue

            if nu > nv:
                nu, nv = nv, nu

            ans.append(self.find_distance(up, nu, nv, LOG))

        return ans

    def find_distance(self, up: list[list[int]], u: int, v: int, LOG: int) -> int:
        jumps = 0

        for i in range(LOG - 1, -1, -1):
            if up[u][i] < v:
                jumps += 1 << i
                u = up[u][i]

        return jumps + 1 if up[u][0] >= v else -1
