class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: "TreeNode | None" = None,
        right: "TreeNode | None" = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        return self.finder(root) != -1

    def finder(self, node: TreeNode | None) -> int:
        if node is None:
            return 0

        left = self.finder(node.left)
        if left is -1:
            return -1
        right = self.finder(node.right)
        if right is -1:
            return -1

        return -1 if abs(left - right) > 1 else max(left, right) + 1
