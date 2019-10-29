#!coding=utf8

import pytest
from ..re import *


@pytest.mark.parametrize(['c', 'valid'], [
    ('a', True),
    ('A', True),
    ('1', True),
    ('.', False),
    ('^', False),
    (',', False),
    ('\t', False),
    ('가', False),
])
def test_is_valid_char(c, valid):
    assert is_valid_char(c) == valid


@pytest.mark.parametrize(['s', 'token', 'next_idx'], [
    ('a', Token(TokenType.CHAR, 'a'), 1),
    ('.', Token(TokenType.SPECIAL_CHAR, '.'), 1),
    (r'\.', Token(TokenType.CHAR, '.'), 2),
    ('|', Token(TokenType.OP_OR), 1),
])
def test__tokenize_one_term__success(s, token, next_idx):
    assert Pattern._tokenize_one_term(s, 0) == (token, next_idx)


@pytest.mark.parametrize(['s'], [
    ('^', ),
    ('\t', ),
    ('\\', ),
])
def test__tokenize_one_term__fail(s):
    with pytest.raises(ValueError):
        Pattern._tokenize_one_term(s, 0)


def test_tokenize():
    assert Pattern._tokenize('ab|c') == [
        Token(TokenType.CHAR, 'a'),
        Token(TokenType.CHAR, 'b'),
        Token(TokenType.OP_OR),
        Token(TokenType.CHAR, 'c'),
    ]


def test_expr_consume():
    assert Term('a').consume('abc', 0) == 1
    assert Term('a').consume('xabc', 1) == 2
    assert SpecialTerm('.').consume('abc', 0) == 1
    with pytest.raises(ConsumeFailException):
        Term('a').consume('xabc', 0)
