class Solution:
    def maxValidPairSum(self, nums: list[int], k: int) -> int:
        n = len(nums)
        maxi: list[int] = [0] * n

        maxi[-1] = nums[-1]

        for i in range(n - 2, -1, -1):
            maxi[i] = max(maxi[i + 1], nums[i])

        ans = 0

        for i in range(n - k):
            ans = max(ans, nums[i] + maxi[i + k])

        return ans

    # Another approach with constant singledispatchmethod
    def maxValidPairSum(self, nums: list[int], k: int) -> int:
        n = len(nums)
        maxi = nums[0]
        ans = 0

        j = k

        while j < n:
            maxi = max(maxi, nums[j - k])
            ans = max(ans, nums[j] + maxi)
            j += 1

        return ans
