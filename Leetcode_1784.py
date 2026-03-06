class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        count = 0
        index = 0
        n = len(s)
        while index < n:
            if s[index] == "1":
                count += 1
                while index < n and s[index] == "1":
                    index += 1

            if count > 1:
                return False
            index += 1
        return True
