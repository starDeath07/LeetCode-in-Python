class Solution:
    def findThePrefixCommonArray(self, A: list[int], B: list[int]) -> list[int]:
        n = len(A)
        freq = [0] * (n + 1)
        ans = [0] * n
        count = 0

        for i in range(n):
            freq[A[i]] += 1
            if freq[A[i]] == 2:
                count += 1
            freq[B[i]] += 1
            if freq[B[i]] == 2:
                count += 1
            ans[i] = count

        return ans
