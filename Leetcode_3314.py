class Solution:
    def minBitwiseArray(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [-1] * n

        for i in range(n):
            for val in range(nums[i]):
                if val | (val + 1) == nums[i]:
                    ans[i] = val
                    break
        return ans
