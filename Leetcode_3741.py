from collections import defaultdict
from typing import DefaultDict


class Solution:
    def minimumDistance(self, nums: list[int]) -> int:
        index_map: DefaultDict[int, list[int]] = defaultdict(list)
        ans = 10**10

        for index, value in enumerate(nums):
            index_map[value].append(index)

        for lst in index_map.values():
            n = len(lst)

            if n >= 3:
                for i in range(n - 2):
                    ans = min(ans, 2 * (lst[i + 2] - lst[i]))

        return -1 if ans == 10**10 else ans
