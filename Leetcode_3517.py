from collections import Counter


class Solution:
    def smallestPalindrome(self, s: str) -> str:
        freq: Counter[str] = Counter(s)
        builder: list[str] = []
        middle: str = ""

        for i in range(26):
            key = chr(ord("a") + i)

            if freq[key] >= 2:
                builder.append(key * (freq[key] // 2))
                freq[key] %= 2

            if freq[key] == 1:
                middle = key

        left: str = "".join(builder)
        return left + middle + left[::-1]
