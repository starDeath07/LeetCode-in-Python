class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        inc = 1
        desc = 1

        for i in range(1, n):
            if nums[i] == (nums[i - 1] + 1) % n:
                inc += 1
            if nums[i - 1] == (nums[i] + 1) % n:
                desc += 1

        if inc == n:
            return 0 if nums[0] == 0 else min(n - nums[0], nums[0] + 2)
        if desc == n:
            return min(n - nums[n - 1], nums[n - 1]) + 1

        return -1
