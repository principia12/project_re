from .common import MetaCharacter
from .utils import is_vaild_character
from collections import deque


def check(pattern: str) -> bool:
    if not isinstance(pattern, str):
        raise ValueError()

    for char in pattern:
        if not MetaCharacter.has_value(char) and not is_vaild_character(char):
            return False
    return True


def exact_match(pattern: str, text: str) -> bool:
    if not check(pattern):
        return False

    exprs = tokenizer(pattern)

    for expr in exprs:
        try:
            result = consume(expr, text)
            if result:
                return True
        except TypeError:
            continue

    return False


def consume(expr: deque, text: str):
    for c in text:
        token = expr.popleft()
        method = token['method']
        data = token['data']

        if not method(c, data):
            raise TypeError

    if expr:
        return False
    else:
        return True


def tokenizer(pattern: str):
    expr = []
    tmp_expr = deque()
    is_escape = False

    for c in pattern:
        if c == '\\':
            is_escape = True
            continue

        if is_escape:
            tmp_expr.append({
                'data': c, 'method': lambda x, y: True if x == y else False
            })
            is_escape = False
            continue

        try:
            if MetaCharacter(c) == MetaCharacter.OP_OR:
                expr.append(tmp_expr)
                tmp_expr = deque()
            elif MetaCharacter(c) == MetaCharacter.WILDCARD:
                tmp_expr.append({
                    'data': c, 'method': lambda x, y: is_vaild_character(x)
                })
        except ValueError:
            tmp_expr.append({
                'data': c, 'method': lambda x, y: True if x == y else False
            })

    expr.append(tmp_expr)
    return expr
