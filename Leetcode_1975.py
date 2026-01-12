from typing import List


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        ans = 0
        count = 0
        minn = 1000000
        for row in matrix:
            for val in row:
                if val < 0:
                    count += 1
                ans += abs(val)
                minn = min(minn, abs(val))
        return ans if count % 2 == 0 else ans - 2 * minn


if __name__ == "__main__":
    ans = Solution().maxMatrixSum([[1, 2], [41]])

    print(ans)
