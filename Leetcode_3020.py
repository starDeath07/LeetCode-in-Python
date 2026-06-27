from collections import Counter


class Solution:
    def maximumLength(self, nums: list[int]) -> int:
        freq = Counter(nums)
        ans = 0

        if 1 in freq:
            if freq[1] % 2:
                ans = freq[1]
            else:
                ans = freq[1] - 1
            del freq[1]

        for key in freq.keys():
            temp = 0

            while key in freq:
                temp += 2
                if freq[key] < 2:
                    break
                key *= key

            ans = max(ans, temp - 1)

        return ans
