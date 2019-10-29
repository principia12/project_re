#!coding=utf8

import pytest

from ..main import check, exact_match


################################################################################
# My Test
################################################################################

@pytest.mark.parametrize(['ptn_str', 'valid'], [
    ('abc', True),
    ('abc|', True),
    ('|abc', True),
    ('1', True),
    ('a', True),
    ('b', True),
    ('abc', True),
    ('^abc', False),
])
def test_check(ptn_str, valid):
    assert check(ptn_str) == valid


@pytest.mark.parametrize(['ptn_str', 'text', 'success'], [
    ('abc', 'abc', True),
    ('', '', True),
    ('a.c', 'abc', True),
    ('abcd', 'abc', False),
    ('ab', 'abc', False),
    ('abc|d', 'abc', True),
    ('abc|d', 'abc', True),
    ('abc|d', 'd', True),
    ('abc|', '', True),
    ('|abc', '', True),
    ('||abc', '', True),
    ('abc|d', 'abcd', False),
    ('|abc', 'a', False),
])
def test_exact_match(ptn_str, text, success):
    assert exact_match(ptn_str, text) == success


@pytest.mark.parametrize(['ptn_str', 'text'], [
    ('^abc', 'abc'),
    ('a,bc', 'abc'),
    (1, 2),
])
def test_exact_match_with_raise(ptn_str, text):
    with pytest.raises(ValueError):
        exact_match(ptn_str, text)


################################################################################
# Shared Test
################################################################################

@pytest.mark.parametrize(['ptn_str', 'valid'], [
    ('abjsdkfj123213dsjklfj', True),
    ('123|122', True),
    ('sdfsdf|122', True),
    ('|122', True),
    ('..|122', True),
    ('..122', True),
    ('adfsdf..122', True),
    ('123|||', True),
    ('가', False),
    ('+123-=-=', False),
    (r'/--*-*', False),
    ('()', False),
    ('123|---', False),
])
def test_check_shared(ptn_str, valid):
    assert check(ptn_str) == valid


@pytest.mark.parametrize(['ptn_str', 'text', 'success'], [
    ('1', '1', True),
    ('.', '1', True),
    ('1', '1', True),
    ('1|2', '1', True),
    ('1|2', '2', True),
    ('.|2', '1', True),
    ('|2', '', True),
    (r'\.', '.', True),
    ('..', '1', False),
    ('..', '1', False),
    ('..|2', '1', False),
    ('..|.2', '1', False),
    ('..|ab', '1', False),
])
def test_exact_match_shared(ptn_str, text, success):
    assert exact_match(ptn_str, text) == success


@pytest.mark.parametrize(['ptn_str', 'text'], [
    (1, 2),
])
def test_exact_match_with_raise_shared(ptn_str, text):
    with pytest.raises(ValueError):
        exact_match(ptn_str, text)
