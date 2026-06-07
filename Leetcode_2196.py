class TreeNode:
    def __init__(
        self, val: int = 0, left: "TreeNode|None" = None, right: "TreeNode|None" = None
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def createBinaryTree(self, descriptions: list[list[int]]) -> TreeNode | None:
        nodes: dict[int, TreeNode] = {}
        childs: set[int] = set()

        for parent, child, isLeft in descriptions:
            if parent not in nodes:
                nodes[parent] = TreeNode(parent)
            if child not in nodes:
                nodes[child] = TreeNode(child)
            childs.add(child)

            if isLeft == 1:
                nodes[parent].left = nodes[child]
            else:
                nodes[parent].right = nodes[child]

        for parent, _, _ in descriptions:
            if parent not in childs:
                return nodes[parent]

        return None
