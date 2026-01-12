from typing import Optional

from leet1161 import TreeNode


class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        left = self.getDepth(root.left)
        right = self.getDepth(root.right)

        if left == right:
            return root
        if left > right:
            return self.subtreeWithAllDeepest(root.left)
        return self.subtreeWithAllDeepest(root.right)

    def getDepth(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        return 1 + max(self.getDepth(node.left), self.getDepth(node.right))
