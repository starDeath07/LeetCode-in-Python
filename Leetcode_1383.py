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
    def balanceBST(self, root: "TreeNode | None") -> "TreeNode | None":
        arr: list[int] = []

        def dfs(node: "TreeNode | None"):
            if node is None:
                return

            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)

        def build(start: int, end: int):
            if start > end:
                return None

            mid = start + (end - start) // 2
            node = TreeNode(arr[mid], build(start, mid - 1), build(mid + 1, end))
            return node

        dfs(root)
        return build(0, len(arr) - 1)
