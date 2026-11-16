class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            temp = []

            for i in range(0, len(s), k):
                total = 0
                for j in range(k):
                    if i + j >= len(s):
                        break
                    total += ord(s[i + j]) - ord("0")

                temp.append(str(total))
            s = "".join(temp)

        return s
