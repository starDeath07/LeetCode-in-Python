class Solution:
    def minimumPrefixLength(self, nums: list[int]) -> int:
        n = len(nums)

        for i in range(n - 1, 0, -1):
            if nums[i - 1] >= nums[i]:
                return i

        return 0
