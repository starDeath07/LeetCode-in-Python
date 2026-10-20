class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        arr = sorted(nums)
        ans = 0

        def rotation(start: int, k: int) -> bool:
            if k == 1:
                return nums[start] == arr[start]

            lsp: list[int] = [0] * k
            length = 0
            i = 1

            while i < k:
                if nums[start + i] == nums[start + length]:
                    length += 1
                    lsp[i] = length
                    i += 1
                elif length != 0:
                    length = lsp[length - 1]
                else:
                    lsp[i] = 0
                    i += 1

            i = 0
            j = 0

            while i < 2 * k:
                if arr[start + j] == nums[start + (i % k)]:
                    i += 1
                    j += 1

                    if j == k:
                        return True
                elif j != 0:
                    j = lsp[j - 1]
                else:
                    i += 1

            return False

        for k in range(1, n + 1):
            if n % k != 0:
                continue

            valid = True

            for start in range(0, n, k):
                if not rotation(start, k):
                    valid = False
                    break

            if valid:
                ans += k

        return ans
