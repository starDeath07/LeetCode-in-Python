class Solution:
    def mapWordWeights(self, words: list[str], weights: list[int]) -> str:
        ans: list[str] = []
        for word in words:
            tot = 0
            for c in word:
                tot += weights[ord(c) - ord("a")]
            tot %= 26
            ans.append(chr(ord("z") - tot))

        return "".join(ans)
