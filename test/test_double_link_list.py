from double_link_list import DoubleLinkList
import pytest


@pytest.mark.parametrize("initial_list, ll, method, params", [
    ([3, 5, 7], DoubleLinkList.from_list([3, 5, 7]), "__len__", ()),
    ([3, 5, 7], DoubleLinkList.from_list([3, 5, 7]), "pop", ()),
    ([3, 5, 7], DoubleLinkList.from_list([3, 5, 7]), "insert", (0, 2)),
    ([3, 5, 7], DoubleLinkList.from_list([3, 5, 7]), "insert", (1, 2)),
    # ([3, 5, 7], DoubleLinkList.from_list([3, 5, 7]), "__delitem__", (0,)),
    # ([3, 5, 7], DoubleLinkList.from_list([3, 5, 7]), "__delitem__", (1,)),
    ([3, 5, 7], DoubleLinkList.from_list([3, 5, 7]), "reverse", ()),
    # ([3], DoubleLinkList.from_list([3]), "reverse", ()),
    # ([], DoubleLinkList.from_list([]), "reverse", ()),
    # ([3, 5, 7], DoubleLinkList.from_list([3, 5, 7]), "clear", ()),
    # ([3, 5, 7], DoubleLinkList.from_list([3, 5, 7]), "extend", ([1, 2, 3],)),
    # ([3, 5, 7], DoubleLinkList.from_list([3, 5, 7]), "sort", ()),
    # ([5, 3, 7], DoubleLinkList.from_list([5, 3, 7]), "sort", ()),
    # ([3, 7, 3], DoubleLinkList.from_list([3, 7, 3]), "sort", ()),
    # ([7, 3], DoubleLinkList.from_list([7, 3]), "sort", ()),
    # ([3], DoubleLinkList.from_list([3]), "sort", ()),
    # ([], DoubleLinkList.from_list([]), "sort", ()),
    # ([3, 5, 7], DoubleLinkList.from_list([3, 5, 7]), "__setitem__", (1, 2)),
    # ([], DoubleLinkList.from_list([]), "__setitem__", (0, 2)),
    # ([3, 5, 7], DoubleLinkList.from_list([3, 5, 7]), "__setitem__", (-1, 2)),
    # ([3, 5, 7], DoubleLinkList.from_list([3, 5, 7]), "__setitem__", (100, 2)),
    #
    # ([3, 5, 7], DoubleLinkList.from_list([3, 5, 7]), "count", (3,)),
    # ([3, 5, 7], DoubleLinkList.from_list([3, 5, 7]), "count", (1,)),
    # ([1, 1, 1], DoubleLinkList.from_list([1, 1, 1]), "count", (1,)),
    # ([1], DoubleLinkList.from_list([1]), "count", (1,)),
    # ([], DoubleLinkList.from_list([]), "count", (1,)),
    # ([None, None], DoubleLinkList.from_list([None, None]), "count", (None,)),
    # ([3, 5, 7], DoubleLinkList.from_list([3, 5, 7]), "index", (7,)),
    # ([3, 3, 3], DoubleLinkList.from_list([3, 3, 3]), "index", (3,)),
    # ([3, 5, 7], DoubleLinkList.from_list([3, 5, 7]), "index", (-1,)),
    # ([3, 5, 7], DoubleLinkList.from_list([3, 5, 7]), "copy", ()),
    # ([3], DoubleLinkList.from_list([3]), "copy", ()),
    # ([], DoubleLinkList.from_list([]), "copy", ()),
    #
    # ([3, 5, 7], DoubleLinkList.from_list([3, 5, 7]), "__add__", ([1, 2, 3],)),
    # ([3, 5, 7], DoubleLinkList.from_list([3, 5, 7]), "__add__", ([1],)),
    # ([3, 5, 7], DoubleLinkList.from_list([3, 5, 7]), "__add__", ([],)),
    # ([3], DoubleLinkList.from_list([3]), "__add__", ([1, 2, 3],)),
    # ([], DoubleLinkList.from_list([]), "__add__", ([1, 2, 3],)),
    # ([], DoubleLinkList.from_list([]), "__add__", ([],)),
    # ([3, 5, 7], DoubleLinkList.from_list([3, 5, 7]), "__contains__", (3,)),
    # ([3, 5, 7], DoubleLinkList.from_list([3, 5, 7]), "__contains__", (1,)),
    # ([3, 5, 7], DoubleLinkList.from_list([3, 5, 7]), "__contains__", (None,)),
    #
    # ([3, 5, 7], DoubleLinkList.from_list([3, 5, 7]), "__mul__", (3,)),
    # ([3, 5, 7], DoubleLinkList.from_list([3, 5, 7]), "__mul__", (0,)),
    # ([3, 5, 7], DoubleLinkList.from_list([3, 5, 7]), "__mul__", (-1,)),


])
def test_all(initial_list, ll, method, params):
    try:
        list_return_value = getattr(initial_list, method)(*params)
    except Exception as e:
        with pytest.raises(type(e)):
            getattr(ll, method)(*params)
    else:

        linked_list_return_value = getattr(ll, method)(*params)
        assert ll == initial_list
        assert linked_list_return_value == list_return_value
