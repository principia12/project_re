
import pytest

from ..common import ConsumeFailException
from ..expression import ClassTerm, Term, AndExpr, OrExpr


def test_class_term__success():
    assert Term('a').consume('a', 0) == 1
    with pytest.raises(ConsumeFailException):
        Term('a').consume('b', 0)


@pytest.mark.parametrize(['class_char', 'text', 'next_idx'], [
    ('d', '1', 1),
    ('D', 'a', 1),
    ('w', '_', 1),
    ('w', 'a', 1),
    ('W', ' ', 1),
    ('W', '.', 1),
    ('s', ' ', 1),
    ('s', '\t', 1),
    ('S', 'a', 1),
])
def test_class_term__success(class_char, text, next_idx):
    assert ClassTerm(class_char).consume(text, 0) == next_idx


@pytest.mark.parametrize(['class_char', 'text'], [
    ('D', '1'),
    ('d', 'a'),
    ('W', '_'),
    ('W', 'a'),
    ('w', ' '),
    ('w', '.'),
    ('S', ' '),
    ('S', '\t'),
    ('s', 'a'),
])
def test_class_term__fail(class_char, text):
    with pytest.raises(ConsumeFailException):
        ClassTerm(class_char).consume(text, 0)


def test_and_expr():
    assert AndExpr([Term('a'), Term('b')]).consume('ab', 0) == 2


def test_or_expr():
    assert OrExpr([Term('a'), Term('b')]).consume('ab', 0) == 1
