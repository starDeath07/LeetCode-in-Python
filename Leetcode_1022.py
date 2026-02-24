class TreeNode:
    def __init__(
        self,
        left: "TreeNode | None" = None,
        right: "TreeNode | None" = None,
        val: int = 0,
    ) -> None:
        self.left = left
        self.right = right
        self.val = val


class Solution:
    def sumRootToLeaf(self, root: TreeNode | None):
        return self.finder(root, 0)

    def finder(self, node: TreeNode | None, curr: int) -> int:
        if node is None:
            return 0
        curr = curr << 1 | node.val
        if node.left is None and node.right is None:
            return curr
        return self.finder(node.left, curr) + self.finder(node.right, curr)
