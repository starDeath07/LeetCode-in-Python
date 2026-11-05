class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        ans = 0

        for a in arr1:
            found = True
            for b in arr2:
                if abs(a - b) <= d:
                    found = False
                    break

            if found:
                ans += 1
        return ans
