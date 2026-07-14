from functools import cache


class Solution:
    def subsequencePairCount(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        def gcd(a: int, b: int) -> int:
            if b == 0:
                return a
            return gcd(b, a % b)

        @cache
        def finder(index: int, g1: int, g2: int) -> int:
            if index == n:
                if g1 > 0 and g2 > 0 and g1 == g2:
                    return 1
                return 0

            skip = finder(index + 1, g1, g2)
            ans = 0
            ans = (ans + finder(index + 1, gcd(g1, nums[index]), g2)) % MOD
            ans = (ans + finder(index + 1, g1, gcd(g1, nums[index]))) % MOD

            return (ans + skip) % MOD

        return finder(0, 0, 0)
