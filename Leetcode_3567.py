class Solution:
    def minAbsDiff(self, grid: list[list[int]], k: int) -> list[list[int]]:
        m, n = len(grid), len(grid[0])
        ans = [[0] * (n - k + 1) for _ in range(m - k + 1)]
        size = k * k
        temp_list = [0] * size
        maxi = 10**10

        for i in range(m - k + 1):
            for j in range(n - k + 1):
                index = 0

                for p in range(i, i + k):
                    for q in range(j, j + k):
                        temp_list[index] = grid[p][q]
                        index += 1

                temp_list.sort()
                diff = maxi
                for z in range(1, size):
                    if temp_list[z] != temp_list[z - 1]:
                        diff = min(diff, temp_list[z] - temp_list[z - 1])
                ans[i][j] = 0 if diff == maxi else diff

        return ans
