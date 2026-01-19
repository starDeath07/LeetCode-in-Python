class Solution:
    def maxSideLength(self, mat: list[list[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        pref: list[list[int]] = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                pref[i][j] = (
                    pref[i - 1][j]
                    + pref[i][j - 1]
                    - pref[i - 1][j - 1]
                    + mat[i - 1][j - 1]
                )

        left: int = 0
        right: int = min(n, m)
        ans: int = 0

        while left <= right:
            mid: int = left + (right - left) // 2
            if self.valid(pref, threshold, mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans

    def valid(self, pref: list[list[int]], threshold: int, side: int) -> bool:
        for i in range(side, len(pref)):
            for j in range(side, len(pref[0])):
                if (
                    pref[i][j]
                    - pref[i - side][j]
                    - pref[i][j - side]
                    + pref[i - side][j - side]
                    <= threshold
                ):
                    return True
        return False
