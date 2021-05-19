import pytest

from hash_map import HashMap

EL_COUNT = 500000


def test_all():
    hash_map = HashMap()
    el_count = EL_COUNT
    for x in range(el_count):
        hash_map.put(str(x), str(x))
    for x in range(el_count):
        assert hash_map.get(str(x)) == str(x)


def test_all_dict():
    hash_map = dict()
    el_count = EL_COUNT
    for x in range(el_count):
        hash_map[str(x)] = str(x)

    for x in range(el_count):
        assert hash_map.get(str(x)) == str(x)
