
from dataclasses import dataclass


class ConsumeFailException(Exception):
    """Match fail"""


class TokenType:
    CHAR, SPECIAL_CHAR, OP_OR = range(3)


@dataclass
class Token:
    token_type: TokenType
    value: str = None


SPECIAL_CHARS = {'.'}
OP_CHARS = {
    '|': TokenType.OP_OR,
}


def is_valid_char(c: str):
    return ('a' <= c <= 'z') or ('A' <= c <= 'Z') or ('0' <= c <= '9')
