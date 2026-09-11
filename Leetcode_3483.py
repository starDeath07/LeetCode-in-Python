class Solution:
    def totalNumbers(self, digits: list[int]) -> int:
        freq: list[int] = [0] * 10
        ans = 0

        for digit in digits:
            freq[digit] += 1

        for i in [0, 2, 4, 6, 8]:
            if freq[i] == 0:
                continue
            freq[i] -= 1

            for j in range(1, 10):
                if freq[j] == 0:
                    continue
                freq[j] -= 1
                ans += sum(1 for x in freq if x > 0)
                freq[j] += 1

            freq[i] += 1
        return ans
