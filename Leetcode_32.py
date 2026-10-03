class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        open, close = 0, 0

        ans = 0

        for i in range(n):
            if s[i] == "(":
                open += 1
            else:
                close += 1

            if open == close:
                ans = max(ans, open + close)
            elif close > open:
                close = open = 0

        open = close = 0

        for i in range(n - 1, -1, -1):
            if s[i] == ")":
                close += 1
            else:
                open += 1

            if open == close:
                ans = max(ans, open + close)
            elif open > close:
                open = close = 0

        return ans

    # Solution with stack
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        stack: list[int] = [-1]
        ans = 0

        for i in range(n):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if len(stack) == 0:
                    stack.append(i)
                else:
                    ans = max(ans, i - stack[-1])

        return ans
