from math import gcd


class Solution:
    def maxLength(self, nums: list[int]) -> int:
        res = 2
        prod = 1
        l = 0

        for r in range(len(nums)):
            while gcd(prod, nums[r]) > 1:
                prod //= nums[l]
                l += 1

            prod *= nums[r]
            res = max(res, r - l + 1)

        return res
