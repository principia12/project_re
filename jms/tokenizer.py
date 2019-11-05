
from dataclasses import dataclass

from .common import is_valid_char


class TokenType:
    CHAR, ANCHOR_CHAR, WILDCARD_CHAR, CLASS_CHAR, OP_CHAR = range(5)


@dataclass
class Token:
    token_type: TokenType
    value: str = None


ANCHOR_CHARS = {'^', '$'}
WILDCARD_CHARS = {'.'}
CLASS_CHARS = {'d', 'D', 'w', 'W', 's', 'S'}
OP_CHARS = {'|'}
SPECIAL_CHARS = set().union(WILDCARD_CHARS, ANCHOR_CHARS, OP_CHARS)


def tokenize(s):
    idx = 0
    tokens = []
    while idx < len(s):
        token, idx = _tokenize_one_term(s, idx)
        tokens.append(token)
    return tokens


def _tokenize_one_term(s, idx):
    c = s[idx]
    if c in OP_CHARS:
        token = Token(TokenType.OP_CHAR, c)
        idx += 1
    elif c in ANCHOR_CHARS:
        token = Token(TokenType.ANCHOR_CHAR, c)
        idx += 1
    elif c in WILDCARD_CHARS:
        token = Token(TokenType.WILDCARD_CHAR, c)
        idx += 1
    elif c == '\\':
        if idx + 1 >= len(s):
            raise ValueError('End with \\')
        c = s[idx + 1]
        if c in SPECIAL_CHARS:
            token = Token(TokenType.CHAR, c)
        elif c in CLASS_CHARS:
            token = Token(TokenType.CLASS_CHAR, c)
        else:
            raise ValueError('Invalid usage of \\')
        idx += 2
    elif is_valid_char(c):
        token = Token(TokenType.CHAR, c)
        idx += 1
    else:
        raise ValueError(f'Invalid Char <{c}>, at {idx}')

    return token, idx


def tokenize_new(s):
    escaping = False
    tokens = []
    for c in s:
        if c == '\\' and not escaping:
            escaping = True
        else:
            tokens.append(_tokenize_one_char(c, escaping))
            escaping = False
    if escaping:
        raise ValueError('Ends with \\')
    return tokens


def _tokenize_one_char(c, escaping):
    if escaping:
        if c in CLASS_CHARS:
            token_type = TokenType.CLASS_CHAR
        elif c in SPECIAL_CHARS:
            token_type = TokenType.CHAR
        else:
            raise ValueError('Invalid usage of \\')
    else:
        if c in OP_CHARS:
            token_type = TokenType.OP_CHAR
        elif c in ANCHOR_CHARS:
            token_type = TokenType.ANCHOR_CHAR
        elif c in WILDCARD_CHARS:
            token_type = TokenType.WILDCARD_CHAR
        else:
            token_type = TokenType.CHAR
    return Token(token_type, c)
