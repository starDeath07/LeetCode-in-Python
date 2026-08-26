class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        ans: str = ""
        start: int = 0
        end: int = 0
        ones: int = 0

        while end < n:
            ones += s[end] == "1"

            while start < end and (s[start] == "0" or ones > k):
                ones -= s[start] == "1"
                start += 1

            if ones == k:
                curr = s[start : end + 1]
                if ans == "" or (len(curr), curr) < (len(ans), ans):
                    ans = s[start : end + 1]

            end += 1

        return ans
