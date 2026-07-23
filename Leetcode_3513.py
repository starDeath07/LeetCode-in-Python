from functools import reduce


class Solution:
    def uniqueXorTriplets(self, nums: list[int]) -> int:
        n = len(nums)
        return n if n <= 2 else reduce(lambda a, b: a | b, nums) + 1
