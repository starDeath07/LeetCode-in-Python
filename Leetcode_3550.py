class Solution:
    def smallestIndex(self, nums: list[int]) -> int:
        n = len(nums)

        for i in range(n):
            if i == self.dig_sum(nums[i]):
                return i

        return -1

    def dig_sum(self, val: int) -> int:
        total = 0
        while val:
            total += val % 10
            val //= 10

        return total
