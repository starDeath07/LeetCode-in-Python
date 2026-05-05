# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return head

        size = 1
        node = head
        curr = head

        while curr.next != None:
            curr = curr.next
            size += 1

        k %= size
        if k == 0:
            return head

        cut = size - k
        while cut > 1:
            node = node.next
            cut -= 1

        curr.next = head
        head = node.next
        node.next = None
        return head
