from typing import Optional


class Node:
    def __init__(self, value: int, left: Optional['Node'] = None, right:  Optional['Node'] = None):
        self.value = value
        self.left = left
        self.right = right


class Tree:
    def __init__(self):
        self.root: Optional[Node] = None

    def insert(self, value: int):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node: Node, value: int):
        if node.value > value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(node.right, value)

    def contains(self, value: int) -> bool:
        if self.root is None:
            return False
        if self.root.value == value:
            return True
        else:
            return self._contains(self.root, value)

    def _contains(self, node: Node, value: int):
        if node.value > value:
            if node.left.value == value:
                return True
            else:
                return self._contains(node.left, value)

        else:
            if node.right.value == value:
                return True
            else:
                return self._contains(node.right, value)

    def as_set(self):
        count = set()
        if self.root is None:
            return count
        else:
            count.add(self.root.value)
            return self._insert_in_set(self.root, count)

    def _insert_in_set(self, node, count):
        if node.left is not None:
            count.add(node.left.value)
            return self._insert_in_set(node.left, count)

        if node.right is not None:
            count.add(node.right.value)
            return self._insert_in_set(node.right, count)

        if node.left is None and node.right is None:
            return count





