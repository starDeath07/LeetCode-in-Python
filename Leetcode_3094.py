class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        maxi: list[int] = [nums[0]]
        mini: list[int] = [10**10] * n
        mini[n - 1] = nums[n - 1]

        for i in range(1, n):
            maxi.append(max(nums[i], maxi[-1]))

        for i in range(n - 2, -1, -1):
            mini[i] = min(mini[i + 1], nums[i])

        ans: int = n + 1

        for i in range(n):
            curr = maxi[i] - mini[i]
            if curr <= k:
                ans = min(ans, i)

        return ans if ans != n + 1 else -1
