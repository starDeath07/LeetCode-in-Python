class Solution:
    def validSequence(self, word1: str, word2: str) -> list[int]:
        n = len(word1)
        m = len(word2)
        ans: list[int] = []
        suffix: list[int] = [0] * (n + 1)
        j = m - 1
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1]
            if j >= 0 and word1[i] == word2[j]:
                suffix[i] += 1
                j -= 1

        i = 0
        j = 0
        matched = False

        while i < n and j < m:
            if word1[i] == word2[j]:
                ans.append(i)
                j += 1
            elif matched is False and suffix[i + 1] >= m - j - 1:
                ans.append(i)
                matched = True
                j += 1
            i += 1

        if j == m:
            return ans

        return []
