class Solution:
    def minimumDeletions(self, s: str) -> int:
        count = 0
        ans = 0

        for i in range(len(s)):
            if s[i] == "b":
                count += 1
            else:
                if count > 0:
                    count -= 1
                    ans += 1
        return ans
