class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        is_sorted: bool = True

        for i in range(1, n):
            if s[i - 1] > s[i]:
                is_sorted = False
                break

        if is_sorted:
            return 0
        if n == 2:
            return -1

        mini: str = s[0]
        maxi: str = s[0]

        for i in range(n):
            mini = min(s[i], mini)
            maxi = max(s[i], maxi)

        if s[0] == mini or s[-1] == maxi:
            return 1

        for i in range(1, n - 1):
            if s[i] == mini or s[i] == maxi:
                return 2

        return 3
