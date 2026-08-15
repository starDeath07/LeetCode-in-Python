class Solution:
    def longestSubsequence(self, nums: list[int]) -> int:
        n = len(nums)
        xor = 0
        is_pos = False

        for i in range(n):
            xor ^= nums[i]
            is_pos |= nums[i]

        if xor > 0:
            return n

        return n - 1 if xor == 0 and is_pos else 0
