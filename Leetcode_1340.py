class Solution:
    def maxJumps(self, arr: list[int], d: int) -> int:
        n = len(arr)
        ans = 0
        self.dp = [-1] * n

        for i in range(n):
            ans = max(ans, 1 + self.finder(arr, d, i))

        return ans

    def finder(self, arr: list[int], d: int, index: int) -> int:
        if index >= len(arr) or index < 0:
            return 0

        if self.dp[index] != -1:
            return self.dp[index]

        vis = 0

        maxi = min(len(arr) - 1, index + d)

        for i in range(index + 1, maxi + 1):
            if arr[index] > arr[i]:
                vis = max(vis, 1 + self.finder(arr, d, i))
            else:
                break

        mini = max(0, index - d)

        for i in range(index - 1, mini - 1, -1):
            if arr[index] > arr[i]:
                vis = max(vis, 1 + self.finder(arr, d, i))
            else:
                break

        self.dp[index] = vis
        return vis
