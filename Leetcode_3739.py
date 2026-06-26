from collections import defaultdict


class Solution:
    def countMajoritySubarrays(self, nums: list[int], target: int) -> int:
        n = len(nums)
        freq: defaultdict[int, int] = defaultdict(int)
        ans, total, valid = 0, 0, 0
        freq[0] = 1

        for i in range(n):
            if nums[i] == target:
                valid += freq[total]
                total += 1
            else:
                total -= 1
                valid -= freq[total]

            ans += valid
            freq[total] += 1
        return ans
