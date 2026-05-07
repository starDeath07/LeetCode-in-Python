class Solution:
    def maxValue(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [0] * n
        maxi = [0] * n
        maxi[0] = nums[0]

        for i in range(1, n):
            maxi[i] = max(maxi[i - 1], nums[i])

        mini = 10**10

        for i in range(n - 1, -1, -1):
            if maxi[i] > mini:
                ans[i] = ans[i + 1]
            else:
                ans[i] = maxi[i]
            mini = min(mini, nums[i])

        return ans
