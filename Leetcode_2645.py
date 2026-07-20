class Solution:
    def addMinimum(self, word: str) -> int:
        n = len(word)
        ans = 0
        index = 0

        while index < n:
            if index < n and word[index] == "a":
                index += 1
            else:
                ans += 1
            if index < n and word[index] == "b":
                index += 1
            else:
                ans += 1
            if index < n and word[index] == "c":
                index += 1
            else:
                ans += 1

        return ans
