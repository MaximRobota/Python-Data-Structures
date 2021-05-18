from typing import Optional, Any


class Node:
    def __init__(self, value: Any, previous: Optional['Node'] = None, other: Optional['Node'] = None):
        self.value = value
        self.previous = previous
        self.other = other

    def append(self, value):
        if self.other is None:
            self.other = Node(value)
            self.other.previous = self
        else:
            self.other.append(value)

    def as_list(self):
        if self.other is None:
            return [self.value]
        else:
            return [self.value] + self.other.as_list()

    def length(self):
        pass

    def length2(self, acc=0):
        acc += 1

        if self.other is None:
            return acc
        else:
            return self.other.length2(acc)

    def node_at(self, index):
        pass

    def remove(self, index):
        pass

    # def reverse(self):
        # tmp_other = self.other
        # tmp_previous = self.previous
        #
        # self.previous = self.other
        # self.other = tmp_previous
        #
        # if tmp_other is None:
        #     return self
        #
        # return tmp_other.reverse(self)
    def reverse(self, new_other=None):  # ????
        old_other = self.other
        self.other = new_other
        if old_other is None:
            return self
        return old_other.reverse()

    def pop(self):
        if self.other.other is None:
            the_next_one = self.other
            self.other = None
            return the_next_one
        return self.other.pop()

    def count(self, value, _count_length=False):
        pass

    def index(self, value, index=0):
        pass

    def sort(self):
        pass

    def set(self, index, value):
        pass

    def copy(self):
        pass

    def contains(self, value):
        pass

    def last(self):
        pass

    def __repr__(self):
        return f"<Node value: {self.value}, other: {None if self.other is None else 'set'}>"


class DoubleLinkList:
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
        length = self.length2()
        node = self.root
        new_el = Node(value)

        if index == 0:
            new_el.other = node
            self.root = new_el
        else:
            if index < length:
                for _ in range(index - 1):
                    if node.other is None:
                        raise IndexError(f"Can not find Node at index: {index}")
                    else:
                        node = node.other
                new_el.other = node.other
                node.other = new_el
            else:
                raise IndexError(f"Can not insert at index: {index}, because length: {length}")

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
        pass

    def pop(self):
        if self.root is None:
            raise IndexError("Empty list")
        return self.root.pop().value  # ????

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
            pass
        else:
            raise IndexError(f"Can not remove at index: {index}, because length: {length}")

    def remove2(self, index: int):
        pass

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
        pass

    def index(self, value):
        if self.root is None:
            raise ValueError(f"{value} is not in list")

        return self.root.index(value)

    def sort(self):
        pass

    @classmethod
    def from_list(cls, a_list: list) -> 'DoubleLinkList':
        ll = DoubleLinkList()
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
        elif isinstance(other, DoubleLinkList):
            return self.as_list() == other.as_list()

    def __add__(self, other: list):
        if self.root is None:
            return DoubleLinkList.from_list(other)
        this_copy = self.copy()
        this_copy.extend(other)
        return this_copy

    def copy(self) -> 'DoubleLinkList':
        ll = DoubleLinkList()
        if self.root is None:
            return ll

        root_copy = self.root.copy()
        ll.root = root_copy
        return ll

    def __mul__(self, factor: int):
        if self.root is None:
            return []

        new_ll = DoubleLinkList()
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
        return f"<DoubleLinkList {self.as_list()}>"
