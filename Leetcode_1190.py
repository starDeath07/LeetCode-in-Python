class Solution:
    def reverseParentheses(self, s: str) -> str:
        def finder(i):
            result = []

            while i < len(s):
                if s[i] == "(":
                    inner, i = finder(i + 1)
                    result.append(inner[::-1])

                elif s[i] == ")":
                    return "".join(result), i + 1

                else:
                    result.append(s[i])
                    i += 1

            return "".join(result), i

        ans, _ = finder(0)
        return ans
