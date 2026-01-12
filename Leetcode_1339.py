from __future__ import annotations


class Solution:
    def maxProduct(self, root: TreeNode | None = None) -> int:
        def total_sum(root) -> int:
            if not root:
                return 0

            return root.val + total_sum(root.left) + total_sum(root.right)

        def get_Prod(root) -> int:
            nonlocal ans
            if not root:
                return 0

            curr = root.val + get_Prod(root.left) + get_Prod(root.right)

            ans = max(ans, curr * (tot - curr))
            return curr

        tot = total_sum(root)
        ans = -10000000000
        get_Prod(root)
        return ans % (10**9 + 7)
