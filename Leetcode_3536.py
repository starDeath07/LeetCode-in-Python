class Solution:
    def maxProduct(self, n: int) -> int:
        freq: list[int] = [0] * 10

        while n:
            freq[n % 10] += 1
            n //= 10

        prev: int = 0
        for i in range(9, -1, -1):
            if freq[i] == 0:
                continue
            if freq[i] > 1:
                return max(i * i, prev * i)
            elif freq[i] != 0 and prev != 0:
                return prev * i
            prev = i

        return 0
