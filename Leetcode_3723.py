class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > num * 9:
            return ""

        ans: list[str] = []

        quotient = sum // 9
        remainder = sum % 9

        ans.extend(["9"] * quotient)

        if remainder > 0:
            ans.append(str(remainder))

        ans.extend(["0"] * (num - len(ans)))

        return "".join(ans)
