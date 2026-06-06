class Solution:
    def leftRightDifference(self, nums: list[int]) -> list[int]:
        n = len(nums)
        right_sum = sum(nums)
        left_sum = 0
        ans: list[int] = []

        for i in range(n):
            right_sum -= nums[i]
            ans.append(abs(left_sum - right_sum))
            left_sum += nums[i]
        return ans
