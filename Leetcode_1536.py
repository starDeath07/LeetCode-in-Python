class Solution:
    def minSwaps(self, grid: list[list[int]]) -> int:
        n = len(grid)
        ans = 0
        count: list[int] = [0] * n

        for i in range(n):
            curr = 0
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 0:
                    curr += 1
                else:
                    break
            count[i] = curr

        for i in range(n):
            need = n - i - 1
            found = False

            for j in range(i, n):
                if count[j] >= need:
                    found = True
                    ans += j - i

                    while j > i:
                        count[j - 1], count[j] = count[j], count[j - 1]
                        j -= 1

                    break
            if not found:
                return -1

        return ans
