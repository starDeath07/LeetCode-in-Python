class Solution:
    def minBitwiseArray(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [-1] * n

        for i in range(n):
            if nums[i] == 2:
                continue
            for j in range(32):
                if nums[i] & (1 << j) == 0:
                    ans[i] = nums[i] ^ (1 << (j - 1))
                    break

        return ans
