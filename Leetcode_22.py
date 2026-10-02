class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans: list[str] = []
        curr: list[str] = []

        def finder(open: int, close: int) -> None:
            if len(curr) == 2 * n:
                ans.append("".join(curr))
                return

            if open < n:
                curr.append("(")
                finder(open + 1, close)
                curr.pop()

            if close < open:
                curr.append(")")
                finder(open, close + 1)
                curr.pop()

        finder(0, 0)
        return ans
