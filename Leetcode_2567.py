class Solution:
    def minimizeSum(self, nums: list[int]) -> int:
        n = len(nums)
        nums.sort()
        # remove first two elements to make it equal to third
        # remove last two elements to make it equal to last third elements
        # remove first element to make it equal to 2nd element and doing the same with last element to make it equal to last 2nd element
        return min(nums[n - 1] - nums[1], nums[n - 3] - nums[0], nums[n - 2] - nums[1])
