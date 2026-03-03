class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        size = (1 << n) - 1
        mid = size // 2

        if n == 1 and k == 1:
            return "0"
        if mid + 1 == k:
            return "1"

        if k < mid + 1:
            return self.findKthBit(n - 1, k)
        else:
            return "1" if self.findKthBit(n - 1, size - k + 1) == "0" else "0"
