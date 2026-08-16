class Solution:
    def stoneGameIX(self, stones: list[int]) -> bool:
        n = len(stones)
        freq: list[int] = [0] * 3

        for i in range(n):
            freq[stones[i] % 3] += 1

        if freq[0] % 2 == 0:
            return freq[1] > 0 and freq[2] > 0
        return abs(freq[2] - freq[1]) > 2
