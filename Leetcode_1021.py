class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans: list[str] = []
        count = 0

        for c in s:
            if c == "(":
                if count:
                    ans.append(c)
                count += 1
            else:
                count -= 1
                if count:
                    ans.append(c)

        return "".join(ans)
