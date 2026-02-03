class Solution:
    def isTrionic(self, nums: list[int]) -> bool:
        n = len(nums)
        i = 0

        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1

        if i == 0 or i == n - 1:
            return False

        prev = i

        while i + 1 < n and nums[i] > nums[i + 1]:
            i += 1

        if i == prev or i == n - 1:
            return False

        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1

        return True if i == n - 1 else False
