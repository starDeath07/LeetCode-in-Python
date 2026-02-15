class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans: list[str] = []
        i, j = len(a) - 1, len(b) - 1
        carry: int = 0

        while i >= 0 or j >= 0:
            sum = carry

            if i >= 0:
                sum += ord(a[i]) - 0
            if j >= 0:
                sum += ord(b[j]) - 0

            ans.append(str(sum % 2))
            carry = sum // 2

        if carry > 0:
            ans.append("1")

        ans.reverse()
        res = "".join(ans)
        return res
