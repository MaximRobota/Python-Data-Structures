from tree import Tree


def test_insert():
    tree = Tree()
    tree.insert(7)
    tree.insert(3)
    tree.insert(11)
    tree.insert(5)
    assert tree.contains(3)


def test_contains_none_existant():
    tree = Tree()
    assert not tree.contains(1)


def test_contains_one_element():
    tree = Tree()
    tree.insert(1)
    assert tree.contains(1)


def test_contains_large_range():
    tree = Tree()
    for i in range(500):
        tree.insert(i)
    assert tree.contains(499)


def test_as_set():
    tree = Tree()
    for i in range(500):
        tree.insert(i)

    assert tree.as_set() == set(range(500))
