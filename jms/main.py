
from .pattern import Pattern


def check(ptn_str):
    try:
        Pattern(ptn_str)
    except ValueError:
        return False
    else:
        return True


def match(ptn_str, text):
    ptn = Pattern(ptn_str)
    return ptn.match(text)


