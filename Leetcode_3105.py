class Solution:
    def longestMonotonicSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        ans, temp = 1, 1

        for i in range(1, n):
            if nums[i - 1] < nums[i]:
                temp += 1
            else:
                temp = 1

            ans = max(ans, temp)

        temp = 1

        for i in range(1, n):
            if nums[i - 1] > nums[i]:
                temp += 1
            else:
                temp = 1

            ans = max(ans, temp)

        return ans
