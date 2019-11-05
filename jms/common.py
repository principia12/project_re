
class ConsumeFailException(Exception):
    """Match fail"""


def split_seq(xs, sep):
    sub = []
    for x in xs:
        if x == sep:
            yield sub
            sub = []
        else:
            sub.append(x)
    yield sub


def is_numeric(c):
    return '0' <= c <= '9'


def is_alpha(c):
    return ('a' <= c <= 'z') or ('A' <= c <= 'Z')


def is_word_char(c):
    return is_alpha(c) or is_numeric(c) or c == '_'


def is_whitespace(c):
    return c == ' ' or c == '\t' or c == '\n' or c == '\r'


def is_valid_char(c: str):
    return is_word_char(c) or is_whitespace(c)


