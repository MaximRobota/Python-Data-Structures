from typing import Optional, Any, Tuple


class Node:
    def __init__(self, value: Any, other: Optional['Node'] = None):
        self.value = value
        self.other = other

    def append(self, value):
        if self.other is None:
            self.other = Node(value)
        else:
            self.other.append(value)

    def as_list(self):
        if self.other is None:
            return [self.value]
        else:
            return [self.value] + self.other.as_list()

    def length(self):
        return self.count(None, _count_length=True)

    def length2(self, acc=0):
        acc += 1

        if self.other is None:
            return acc
        else:
            return self.other.length2(acc)

    def node_at(self, index):
        if index == 0:
            return self
        else:
            return self.other.node_at(index - 1)

    def remove(self, index):
        if index == 0:
            return

        if index == 1:
            self.other = self.other.other
            return
        self.other.remove(index - 1)

    def remove_by(self, predicate, root: Optional['Node'] = None) -> Tuple[Optional['Node'], Optional[Any]]:
        if root is None:
            root = self
        if self is root and predicate(self.value):
            return self.other, None

        if self.other:
            if predicate(self.other.value):
                self.other = self.other.other
                return root, self.other.value
            else:
                return self.other.remove_by(predicate, root=root)
        else:
            return root, None

    def for_each(self, consumer):
        consumer(self.value)
        if self.other:
            self.other.for_each(consumer)

    def get_by(self, predicate) -> Optional[Any]:
        if predicate(self.value):
            return self.value

        if self.other is None:
            return None

        return self.other.get_by(predicate)

    def reverse(self, new_other=None): # ????
        old_other = self.other
        self.other = new_other
        if old_other is None:
            return self
        return old_other.reverse(self)

    def pop(self):
        if self.other.other is None:
            the_next_one = self.other
            self.other = None
            return the_next_one
        return self.other.pop()

    def count(self, value, _count_length=False):
        if _count_length or self.value == value:
            count_here = 1
        else:
            count_here = 0

        if self.other is None:
            return count_here
        else:
            return count_here + self.other.count(value, _count_length=_count_length)

    def index(self, value, index=0):
        if self.value == value:
            return index
        if self.other is None:
            raise ValueError(f"{value} is not in list")
        return self.other.index(value, index + 1)

    def sort(self):
        if self.other is None:
            return

        if self.value <= self.other.value:
            self.other.sort()
            return
        other_value = self.other.value
        self.other.value = self.value
        self.value = other_value

    def set(self, index, value):
        if index == 0:
            self.value = value
            return
        if self.other is None:
            raise IndexError("list assignment index out of range")

        self.other.set(index - 1, value)

    def copy(self):
        if self.other is None:
            return Node(value=self.value)
        return Node(value=self.value, other=self.other.copy())

    def contains(self, value):
        if self.value == value:
            return True
        if self.other is None:
            return False

        return self.other.contains(value)

    def last(self):
        if self.other is None:
            return self
        return self.other.last()

    def __repr__(self):
        return f"<Node value: {self.value}, other: {None if self.other is None else 'set'}>"


class LinkedList:
    def __init__(self):
        self.root: Optional[Node] = None

    def length(self):
        if self.root is None:
            return 0
        else:
            return self.root.length()

    def length2(self):
        if self.root is None:
            return 0
        else:
            return self.root.length2()

    def append(self, value: int):
        if self.root is None:
            self.root = Node(value)
        else:
            self.root.append(value)
        pass

    def insert(self, index: int, value: int):
        length = self.length()
        if index < length:
            new_node = Node(value)
            if index == 0:
                new_node.other = self.root
                self.root = new_node
            else:
                head = self.node_at(index - 1)
                tail = head.other

                new_node.other = tail
                head.other = new_node
        else:
            raise IndexError(f"Can not insert at index: {index}, because length: {length}")
        pass

    def node_at(self, index):
        if index < 0:
            raise IndexError(f"Index must be positive, was: {index}")
        node = self.root
        for _ in range(index):
            if node.other is None:
                raise IndexError(f"Can not find Node at index: {index}")
            node = node.other
        return node

    def pop_first(self):
        if self.root is None:
            raise IndexError("Empty list")
        value = self.root.value
        self.root = self.root.other
        return value

    def pop(self):
        if self.root is None:
            raise IndexError("Empty list")
        return self.root.pop().value

    def crazy_pop(self):
        if self.root is None:
            raise IndexError("Empty list")
        self.reverse()
        value = self.pop_first()
        self.reverse()
        return value

    def remove(self, index: int):
        length = self.length()
        if index < length:
            if index == 0:
                self.pop_first()
            else:
                head = self.node_at(index - 1)
                head.other = head.other.other
        else:
            raise IndexError(f"Can not remove at index: {index}, because length: {length}")

    def remove2(self, index: int):
        length = self.length()
        if index < length:
            if index == 0:
                self.pop_first()
            else:
                self.root.remove(index)
        else:
            raise IndexError(f"Can not remove at index: {index}, because length: {length}")

    def reverse(self):
        if self.root is None:
            return
        self.root = self.root.reverse()

    def clear(self):
        self.root = None

    def count(self, value):
        if self.root is None:
            return 0
        return self.root.count(value)

    def as_list(self):
        if self.root is None:
            return []
        else:
            return self.root.as_list()

    def last_node(self) -> Optional[Node]:
        length = len(self)
        if length == 0:
            return None
        return self.node_at(length - 1)

    def extend(self, a_list: list):
        ll = LinkedList.from_list(a_list)
        this_last_node = self.last_node()
        if not this_last_node:
            self.root = ll.root
            return
        this_last_node.other = ll.root

    def index(self, value):
        if self.root is None:
            raise ValueError(f"{value} is not in list")

        return self.root.index(value)

    def sort(self):
        if self.root is None or self.root.other is None:
            return
        return self.root.sort()

    @classmethod
    def from_list(cls, a_list: list) -> 'LinkedList':
        ll = LinkedList()
        for el in a_list:
            ll.append(el)
        return ll

    def __len__(self):
        return self.length2()

    def __delitem__(self, key):
        self.remove2(key)

    def __setitem__(self, key, value):
        length = len(self)
        if key >= len(self):
            raise IndexError("list assignment index out of range")
        if key < 0:
            key = length + key
        self.root.set(key, value)

    def __eq__(self, other):
        if isinstance(other, list):
            return self.as_list() == other
        elif isinstance(other, LinkedList):
            return self.as_list() == other.as_list()

    def __add__(self, other: list):
        if self.root is None:
            return LinkedList.from_list(other)
        this_copy = self.copy()
        this_copy.extend(other)
        return this_copy

    def copy(self) -> 'LinkedList':
        ll = LinkedList()
        if self.root is None:
            return ll

        root_copy = self.root.copy()
        ll.root = root_copy
        return ll

    def __mul__(self, factor: int):
        if self.root is None:
            return []

        new_ll = LinkedList()
        last_node = None
        for _ in range(factor):
            a_copy = self.root.copy()

            if last_node is None:
                new_ll.root = a_copy
            else:
                last_node.other = a_copy
            last_node = a_copy.last()
        return new_ll

    def __contains__(self, value):
        if self.root is None:
            return False

        return self.root.contains(value)

    def __repr__(self):
        return f"<LinkedList {self.as_list()}>"
