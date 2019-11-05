
from .common import ConsumeFailException, split_seq
from .tokenizer import tokenize, TokenType, Token
from .expression import Expr

TOKEN_SEP = Token(TokenType.OP_CHAR, '|')


class Pattern:

    def __init__(self, s):
        if not isinstance(s, str):
            raise ValueError()
        self.root_expr = self._build(tokenize(s))

    def match(self, text):
        if not isinstance(text, str):
            raise ValueError()

        # TODO 효율을 위해 '^', '$'를 위한  shortcut 로직 추가
        for start_idx in range(max(1, len(text))):
            try:
                self.root_expr.consume(text, start_idx)
                return True
            except ConsumeFailException:
                pass
        return False

    @staticmethod
    def _build(tokens):
        or_exprs = []
        for sub_tokens in split_seq(tokens, TOKEN_SEP):
            exprs = [Expr.from_token(token) for token in sub_tokens]
            or_exprs.append(Expr.with_and(exprs))
        return Expr.with_or(or_exprs)
