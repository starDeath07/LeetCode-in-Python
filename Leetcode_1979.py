import math


class Solution:
    def findGCD(self, nums: list[int]) -> int:
        return math.gcd(max(nums), min(nums))
