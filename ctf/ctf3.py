import pickle
from collections import defaultdict


class Node:
    def __init__(self, freq: int, data: str, left: 'Node', right: 'Node', _count: int):
        self.right = right
        self.left = left
        self.data = data
        self.freq = freq
        self._count = _count


node: Node = pickle.load(open("ctf/assets/ctf3/node_data.txt", "rb"))


def char_for_bit(node: Node, bit: str) -> Node:
    if bit == "0":
        return node.left
    else:
        return node.right


def is_unique(cypher_text):
    return len(set(cypher_text)) == len(cypher_text)


with open("ctf/assets/ctf3/info.txt") as f:
    current_node = node
    s = ""
    for bit in f.read():
        current_node = char_for_bit(current_node, bit)
        if current_node.data != "\x00":
            assert current_node.left is None
            assert current_node.right is None
            print(f"{current_node.data}")
            s += current_node.data
            current_node = node

    print(s)
    print()
    print(len(set(s)))
    # import codecs
    # print(codecs.encode(s.encode(), "hex"))

    # d = dict(zip("VG9ue", "what "))
    # table = str.maketrans(d)
    # candidate = s.translate(table)
    # print(candidate)
    # known_text = " flag{"
    # i = 0
    # for i in range(len(s)-len(known_text)):
    #     cypher_text = s[i:len(known_text)+i]
    #     if not is_unique(cypher_text):
    #         continue
    #     d = dict(zip(cypher_text, known_text))
    #     d.update({"W": "_"})
    #     table = str.maketrans(d)
    #     candidate = s.translate(table)
    #     if candidate.count("{") == 1:
    #         # print(table)
    #         print(candidate)
    # for i in range(12):
    #     for j in range(i, len(s), 12):
    #         print(s[j], end="")
    #     print()
    d = defaultdict(int)
    for char in s:
        d[char] += 1
    for letter, frq in sorted(d.items(), key=lambda a: a[1]):
        print(letter, frq)
    d = dict(zip("9VF2bXZf", " etaoins"))
    table = str.maketrans(d)
    candidate = s.translate(table)
    print(candidate)
