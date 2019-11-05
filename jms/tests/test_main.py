#!coding=utf8

import pytest

from ..main import check, match


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
    ('^abc', True),
])
def test_check(ptn_str, valid):
    assert check(ptn_str) == valid


@pytest.mark.parametrize(['ptn_str', 'text', 'success'], [
    ('abc', 'abc', True),
    ('', '', True),
    ('a.c', 'abc', True),
    ('abcd', 'abc', False),
    ('bc', 'abc', True),
    ('ab', 'abc', True),
    ('abc|d', 'abc', True),
    ('abc|d', 'abc', True),
    ('abc|d', 'd', True),
    ('abc|', '', True),
    ('|abc', '', True),
    ('||abc', '', True),
    ('abc|d', 'abcd', True),
    ('abc', 'a', False),
    ('^ab', 'abc', True),
    ('^ab', 'xabc', False),
    ('bc$', 'abc', True),
    ('bc$', 'abcy', False),
    ('^$', '', True),
    ('^$', 'a', False),
    (r'a\d', 'a0', True),
    (r'a\D', 'ab', True),
    (r'a\sb', 'a\tb', True),
])
def test_exact_match(ptn_str, text, success):
    assert match(ptn_str, text) == success
