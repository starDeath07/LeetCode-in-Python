import math


class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0
        prefix_gcd: list[int] = []
        maxi = 0

        for i in range(n):
            maxi = max(maxi, nums[i])
            prefix_gcd.append(math.gcd(nums[i], maxi))

        prefix_gcd.sort()
        start = 0
        end = n - 1

        while start < end:
            ans += math.gcd(prefix_gcd[start], prefix_gcd[end])
            start += 1
            end -= 1

        return ans
