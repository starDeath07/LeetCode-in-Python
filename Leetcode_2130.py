class ListNode:
    def __init__(self, val: int = 0, next: "ListNode|None" = None) -> None:
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: ListNode) -> int:
        ans = 0
        curr: ListNode | None = head
        nums: list[int] = []

        while curr:
            nums.append(curr.val)
            curr = curr.next

        n = len(nums)

        for i in range(n // 2):
            ans = max(ans, nums[i] + nums[n - 1 - i])
        return ans
