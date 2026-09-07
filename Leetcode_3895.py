from collections import defaultdict


class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        freq: defaultdict[int, int] = defaultdict(int)

        for num in nums:
            for ch in str(num):
                freq[ord(ch) - ord("0")] += 1

        return freq[digit]
