class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        n = len(arr)
        ans: list[int] = [0] * n
        if n == 0:
            return ans
        index_map: list[tuple[int, int]] = []

        for index, val in enumerate(arr):
            index_map.append((val, index))

        index_map.sort()

        ans[index_map[0][1]] = 1

        for i in range(1, n):
            if index_map[i - 1][0] != index_map[i][0]:
                ans[index_map[i][1]] += ans[index_map[i - 1][1]] + 1
            else:
                ans[index_map[i][1]] = ans[index_map[i - 1][1]]

        return ans
