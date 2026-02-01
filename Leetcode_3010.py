class Solution:
    def minimumCost(self, nums: list[int]) -> int:
        ans = nums[0]
        min1 = min2 = 10**10

        for i in range(1, len(nums)):
            if nums[i] <= min1:
                min2 = min1
                min1 = nums[i]
            elif nums[i] < min2:
                min2 = nums[i]

        return ans + min1 + min2
