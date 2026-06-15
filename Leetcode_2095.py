class ListNode:
    def __init__(self, val: int = 0, next: "ListNode|None" = None) -> None:
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:
        if head is None:
            return head
        if head.next is None:
            return None
        if head.next.next is None:
            head.next = None
            return head

        prev: ListNode | None = None
        slow: ListNode | None = head
        fast: ListNode | None = head

        while fast is not None and fast.next is not None:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = slow.next
        slow.next = None
        return head
