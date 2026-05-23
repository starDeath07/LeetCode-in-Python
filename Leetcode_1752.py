class Solution:
    def check(self, nums: list[int]) -> bool:
        n = len(nums)
        peak = 0
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                peak += 1

        if nums[-1] > nums[0]:
            peak += 1

        return peak < 2
