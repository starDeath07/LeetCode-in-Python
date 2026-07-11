from collections import defaultdict


class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        map: defaultdict[int, int] = defaultdict(int)

        for i in range(n - 1, -1, -1):
            if nums[i] in map:
                return (i + 3) // 3
            map[nums[i]] = i

        return 0
