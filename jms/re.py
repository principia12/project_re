
from abc import ABC, abstractmethod

from .common import Token, TokenType, ConsumeFailException, SPECIAL_CHARS, OP_CHARS, is_valid_char


class Pattern:
    def __init__(self, s):
        if not isinstance(s, str):
            raise ValueError()
        tokens = self._tokenize(s)
        self.or_exprs = self._build(tokens)

    def exact_match(self, text):
        if not isinstance(text, str):
            raise ValueError()
        for expr in self.or_exprs:
            try:
                if expr.consume(text, 0) == len(text):
                    return True
            except ConsumeFailException:
                continue
        return False

    @staticmethod
    def _tokenize(s):
        idx = 0
        tokens = []
        while idx < len(s):
            token, idx = Pattern._tokenize_one_term(s, idx)
            tokens.append(token)
        return tokens

    @staticmethod
    def _tokenize_one_term(s, idx):
        c = s[idx]
        if c in OP_CHARS:
            token = Token(OP_CHARS[c])
            idx += 1
        elif c in SPECIAL_CHARS:
            token = Token(TokenType.SPECIAL_CHAR, c)
            idx += 1
        elif c == '\\':
            if idx + 1 < len(s) and s[idx + 1] in SPECIAL_CHARS:
                token = Token(TokenType.CHAR, s[idx + 1])
            else:
                raise ValueError(f'Invalid SpecialCharacter, at {idx}')
            idx += 2
        elif is_valid_char(c):
            token = Token(TokenType.CHAR, c)
            idx += 1
        else:
            raise ValueError(f'Invalid Char <{c}>, at {idx}')

        return token, idx

    def _build(self, tokens):
        or_exprs = []
        exprs = AndExpr(EmptyTerm())
        for token in tokens:
            if token.token_type == TokenType.OP_OR:
                or_exprs.append(exprs)
                exprs = AndExpr(EmptyTerm())
            else:
                expr = self._make_term(token)
                exprs.add(expr)
        or_exprs.append(exprs)

        return or_exprs

    @staticmethod
    def _make_term(token):
        if token.token_type == TokenType.CHAR:
            return Term(token.value)
        elif token.token_type == TokenType.SPECIAL_CHAR:
            return SpecialTerm(token.value)
        else:
            raise ValueError()


class Expr(ABC):
    @abstractmethod
    def consume(self, text, idx):
        pass


class EmptyTerm(Expr):
    def consume(self, text, idx):
        return idx


class Term(Expr):
    def __init__(self, c):
        self.c = c

    def consume(self, text, idx):
        if idx < len(text) and text[idx] == self.c:
            return idx + 1
        else:
            raise ConsumeFailException()


class SpecialTerm(Expr):
    def __init__(self, c):
        self.c = c

    def consume(self, text, idx):
        if self.c == '.':
            if idx < len(text) and is_valid_char(text[idx]):
                return idx + 1
            else:
                raise ConsumeFailException()


class AndExpr(Expr):
    def __init__(self, expr):
        self.exprs = [expr]

    def add(self, expr):
        self.exprs.append(expr)

    def consume(self, text, idx):
        for expr in self.exprs:
            idx = expr.consume(text, idx)
        return idx
