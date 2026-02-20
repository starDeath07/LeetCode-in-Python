class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        if len(s) == 2:
            return s
        segments: list[str] = []
        index = 0
        curr_sum = 0

        for i in range(len(s)):
            curr_sum += 1 if s[i] == "1" else -1

            if curr_sum == 0:
                sub = s[index + 1 : i]
                part = self.makeLargestSpecial(sub)
                segments.append("1" + part + "0")
                index = i + 1

        return "".join(sorted(segments, reverse=True))
