class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0

        for i in range(n):
            nums[i] *= nums[i]

        nums.sort()

        left, right = 0, n - 1

        while left < right:
            ans += nums[right]
            ans -= nums[left]
            left += 1
            right -= 1

        if left == right:
            ans += nums[left]

        return ans
