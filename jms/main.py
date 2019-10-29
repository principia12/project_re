
from .re import Pattern


def check(ptn_str):
    try:
        Pattern(ptn_str)
    except ValueError:
        return False
    else:
        return True


def exact_match(ptn_str, text):
    ptn = Pattern(ptn_str)
    return ptn.exact_match(text)


