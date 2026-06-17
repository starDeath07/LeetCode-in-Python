class Solution:
    def processStr(self, s: str, k: int) -> str:
        n = len(s)
        lens = [0] * n
        length = 0

        for i, c in enumerate(s):
            if c == "*":
                length = max(length - 1, 0)
            elif c == "#":
                length *= 2
            elif c != "%":
                length += 1

            lens[i] = length

        if k >= length:
            return "."

        i = n - 1
        while True:
            c = s[i]

            if c == "*":
                pass

            elif c == "#":
                if k >= lens[i] // 2:
                    k -= lens[i] // 2

            elif c == "%":
                k = lens[i] - 1 - k

            else:
                if lens[i] == k + 1:
                    return c

            i -= 1
