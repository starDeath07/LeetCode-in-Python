from collections import defaultdict


class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0

        for i in range(n):
            freq: defaultdict[int, int] = defaultdict(int)

            for j in range(i, n):
                freq[nums[j]] += 1
                ans += len(freq) * len(freq)

        return ans
