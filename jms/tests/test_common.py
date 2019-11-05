
from ..common import split_seq


def test_split_seq():
    assert list(split_seq([1, 0, 2, 0, 3], 0)) == [[1], [2], [3]]
    assert list(split_seq([1, 2, 0, 3], 0)) == [[1, 2], [3]]
    assert list(split_seq([1, 2, 0], 0)) == [[1, 2], []]
    assert list(split_seq([1, 2], 0)) == [[1, 2]]
    assert list(split_seq([], 0)) == [[]]
