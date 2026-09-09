class Solution:
    def countCommas(self, n: int) -> int:
        limit = 999
        ans = 0
        while n > limit:
            ans += n - limit
            limit = limit * 1000 + 999
        return ans
