from collections import defaultdict


class Solution:
    def minCost(self, nums1: list[int], nums2: list[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        ans = 0

        if n != m:
            return -1

        mapping: defaultdict[int, int] = defaultdict(int)

        for i in range(n):
            mapping[nums1[i]] += 1
            mapping[nums2[i]] -= 1

        for value in mapping.values():
            value = abs(value)
            if value % 2 != 0:
                return -1
            ans += value >> 1

        return ans >> 1
