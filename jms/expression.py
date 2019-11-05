
from abc import ABC, abstractmethod

from .common import ConsumeFailException, is_valid_char, is_whitespace, is_word_char, is_numeric
from .tokenizer import TokenType


class Expr(ABC):
    @abstractmethod
    def consume(self, text, idx):
        pass

    @classmethod
    def from_token(cls, token):
        if token.token_type == TokenType.CHAR:
            return Term(token.value)
        elif token.token_type == TokenType.ANCHOR_CHAR:
            return AnchorTerm(token.value)
        elif token.token_type in [TokenType.CLASS_CHAR, TokenType.WILDCARD_CHAR]:
            return ClassTerm(token.value)
        else:
            raise ValueError()

    @classmethod
    def with_and(cls, exprs):
        return AndExpr(exprs)

    @classmethod
    def with_or(cls, exprs):
        return OrExpr(exprs)

    @staticmethod
    def get_char(text, idx):
        if idx >= len(text):
            raise ConsumeFailException()
        return text[idx]


class EmptyTerm(Expr):
    def consume(self, text, idx):
        return idx


class Term(Expr):
    def __init__(self, c):
        self.c = c

    def consume(self, text, idx):
        c = self.get_char(text, idx)
        if c == self.c:
            return idx + 1
        else:
            raise ConsumeFailException()


class AnchorTerm(Expr):
    check_funcs = {
        '^': lambda text, idx: idx == 0,
        '$': lambda text, idx: idx == len(text)
    }

    def __init__(self, c):
        self.check_func = self.check_funcs[c]

    def consume(self, text, idx):
        if self.check_func(text, idx):
            return idx
        else:
            raise ConsumeFailException()


class ClassTerm(Expr):
    check_funcs = {
        '.': is_valid_char,
        'd': is_numeric,
        'w': is_word_char,
        's': is_whitespace,
    }

    def __init__(self, c: str):
        self.positive = c == '.' or c.islower()
        self.check_func = self.check_funcs[c.lower()]

    def consume(self, text, idx):
        c = self.get_char(text, idx)
        if self.check_func(c) == self.positive:
            return idx + 1
        else:
            raise ConsumeFailException()


class AndExpr(Expr):
    def __init__(self, exprs):
        self.exprs = exprs

    def consume(self, text, idx):
        for expr in self.exprs:
            idx = expr.consume(text, idx)
        return idx


class OrExpr(Expr):
    def __init__(self, exprs):
        self.exprs = exprs

    def consume(self, text, idx):
        for expr in self.exprs:
            try:
                return expr.consume(text, idx)
            except ConsumeFailException:
                pass
        raise ConsumeFailException()
