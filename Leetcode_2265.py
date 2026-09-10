class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        ans = 0

        def finder(node: TreeNode) -> list[int]:
            nonlocal ans
            if node is None:
                return [0, 0]
            left: list[int] = finder(node.left)
            right: list[int] = finder(node.right)

            total = node.val + left[0] + right[0]
            count = 1 + left[1] + right[1]

            if total // count == node.val:
                ans += 1

            return [total, count]

        finder(root)
        return ans
