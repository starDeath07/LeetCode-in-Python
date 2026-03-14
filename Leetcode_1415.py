class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        # there can be 3 candidates for first place and for the rest of the place there are only 2 candidates as s[i]!=s[i + 1]
        total = 3 * (1 << (n - 1))
        if k > total:
            return ""

        ans: list[str] = []
        size = total // 3

        for c in "abc":
            if k > size:
                k -= size
            else:
                ans.append(c)
                break

        for i in range(1, n):
            size >>= 1
            prev = ans[i - 1]

            for c in "abc":
                if prev != c:
                    if k > size:
                        k -= size
                    else:
                        ans.append(c)
                        break

        return "".join(ans)
