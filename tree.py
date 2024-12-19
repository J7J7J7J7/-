# tree.py
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return TreeNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        return node

    def find_lca(self, x, y):
        return self._find_lca(self.root, x, y)

    def _find_lca(self, node, x, y):
        if not node:
            return None

        # 如果 x 和 y 都小于当前节点，递归到左子树
        if x < node.key and y < node.key:
            return self._find_lca(node.left, x, y)
        # 如果 x 和 y 都大于当前节点，递归到右子树
        if x > node.key and y > node.key:
            return self._find_lca(node.right, x, y)

        return node
