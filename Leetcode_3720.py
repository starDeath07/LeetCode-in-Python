class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        ans: list[str] = []
        freq: list[int] = [0] * 26

        for c in s:
            freq[ord(c) - ord("a")] += 1

        if self.finder(0, freq, target, ans, False):
            return "".join(ans)

        return ""

    def finder(
        self, index: int, freq: list[int], target: str, ans: list[str], found: bool
    ) -> bool:
        if index >= len(target):
            return found

        for i in range(26):
            c = chr(ord("a") + i)
            if freq[i] == 0:
                continue

            if not found and c < target[index]:
                continue

            found = found or c > target[index]
            freq[i] -= 1
            ans.append(c)

            if self.finder(index + 1, freq, target, ans, found):
                return True

            ans.pop()
            freq[i] += 1

        return False
