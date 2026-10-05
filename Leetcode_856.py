class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        n = len(s)
        count = 0
        ans = 0

        for i in range(n):
            if s[i] == "(":
                count += 1
            else:
                count -= 1
                if s[i - 1] == "(":
                    ans += 1 << count

        return ans
