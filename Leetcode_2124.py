class Solution:
    def checkString(self, s: str) -> bool:
        for i in range(1, len(s)):
            if s[i - 1] > s[i]:
                return False

        return True
