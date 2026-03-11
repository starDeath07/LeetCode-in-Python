class Solution:
    def bitwiseComplement(self, n: int) -> int:
        mask = 1

        while n > mask:
            mask = (mask << 1) | 1

        return n ^ mask
