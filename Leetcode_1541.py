class Solution:
    def minInsertions(self, s: str) -> int:
        open = 0
        close = 0

        for c in s:
            if c == "(":
                if close % 2 == 1:
                    open += 1
                    close -= 1
                close += 2
            else:
                close -= 1
                if close < 0:
                    open += 1
                    close = 1

        return open + close
