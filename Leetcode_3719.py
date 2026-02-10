class Solution:
    def longestBalanced(self, nums: list[int]) -> int:
        n = len(nums)
        maxi = 0

        for i in range(n):
            distinct_odd: set[int] = set()
            distinct_even: set[int] = set()
            for j in range(i, n):
                if nums[j] % 2 == 0:
                    distinct_even.add(nums[j])
                else:
                    distinct_odd.add(nums[j])

                if len(distinct_odd) == len(distinct_even):
                    maxi = max(maxi, j - i + 1)
        return maxi
