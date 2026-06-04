class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        ans = 0

        for i in range(num1, num2 + 1):
            val = str(i)
            for j in range(1, len(val) - 1):
                if val[j - 1] < val[j] > val[j + 1]:
                    ans += 1
                elif val[j - 1] > val[j] < val[j + 1]:
                    ans += 1

        return ans
