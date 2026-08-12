from collections import defaultdict


class Solution:
    def maxSubarrayLength(self, nums: list[int], k: int) -> int:
        n = len(nums)
        freq: defaultdict[int, int] = defaultdict(int)
        start = 0
        end = 0
        ans = 0

        while end < n:
            freq[nums[end]] += 1
            while freq[nums[end]] > k:
                freq[nums[start]] -= 1
                if freq[nums[start]] == 0:
                    del freq[nums[start]]
                start += 1
            ans = max(ans, end - start + 1)
            end += 1

        return ans
