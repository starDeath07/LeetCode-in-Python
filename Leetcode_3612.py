class Solution:
    def processStr(self, s: str) -> str:
        res: list[str] = []

        for c in s:
            if c == "#":
                res.extend(res)
            elif c == "%":
                res.reverse()
            elif c == "*":
                if res:
                    res.pop()
            else:
                res.append(c)
        return "".join(res)
