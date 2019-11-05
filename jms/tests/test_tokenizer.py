
import pytest
from ..tokenizer import is_valid_char, Token, TokenType, tokenize, _tokenize_one_term


@pytest.mark.parametrize(['c', 'valid'], [
    ('a', True),
    ('A', True),
    ('1', True),
    ('.', False),
    ('\t', True),
    ('^', False),
    (',', False),
    ('가', False),
])
def test_is_valid_char(c, valid):
    assert is_valid_char(c) == valid


@pytest.mark.parametrize(['s', 'token', 'next_idx'], [
    ('a', Token(TokenType.CHAR, 'a'), 1),
    ('.', Token(TokenType.WILDCARD_CHAR, '.'), 1),
    (r'\.', Token(TokenType.CHAR, '.'), 2),
    ('|', Token(TokenType.OP_CHAR, '|'), 1),
    (r'\d', Token(TokenType.CLASS_CHAR, 'd'), 2),
    (r'\W', Token(TokenType.CLASS_CHAR, 'W'), 2),
    ('^', Token(TokenType.ANCHOR_CHAR, '^'), 1),
    (r'\^', Token(TokenType.CHAR, '^'), 2),
])
def test__tokenize_one_term__success(s, token, next_idx):
    assert _tokenize_one_term(s, 0) == (token, next_idx)


@pytest.mark.parametrize(['s'], [
    (',', ),
    ('\\', ),
])
def test__tokenize_one_term__fail(s):
    with pytest.raises(ValueError):
        _tokenize_one_term(s, 0)


def test_tokenize():
    assert tokenize(r'ab|c.\.') == [
        Token(TokenType.CHAR, 'a'),
        Token(TokenType.CHAR, 'b'),
        Token(TokenType.OP_CHAR, '|'),
        Token(TokenType.CHAR, 'c'),
        Token(TokenType.WILDCARD_CHAR, '.'),
        Token(TokenType.CHAR, '.'),
    ]
