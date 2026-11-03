class Solution:
    def minMoves(self, nums: list[int]) -> int:
        maxi = max(nums)
        ans = 0

        for x in nums:
            ans += abs(maxi - x)

        return ans
