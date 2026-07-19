class Solution:
    def smallestSubsequence(self, s: str) -> str:
        n = len(s)
        ans: list[str] = []
        last_index: list[int] = [0] * 26
        seen: list[bool] = [False] * 26

        for i in range(n):
            last_index[ord(s[i]) - ord("a")] = i

        for i in range(n):
            index = ord(s[i]) - ord("a")
            if seen[index]:
                continue

            while ans and ans[-1] > s[i] and last_index[ord(ans[-1]) - ord("a")] > i:
                seen[ord(ans[-1]) - ord("a")] = False
                ans.pop()

            seen[index] = True
            ans.append(s[i])

        return "".join(ans)
