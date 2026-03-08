class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        n = len(nums)
        ans: list[str] = []

        for i in range(n):
            ans.append("1" if nums[i][i] == "0" else "0")

        return "".join(ans)
