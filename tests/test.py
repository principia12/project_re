from tests.testing_util import *
from pprint import pprint 

@testing
def test():
    assert_member('check')
    assert_member('exact_match')
    
    # check whether given pattern is a valid regular expression. 
    assert_true(check('1'))
    assert_true(check('a'))
    assert_true(check('b'))
    assert_true(check('abc'))
    assert_true(check('abjsdkfj123213dsjklfj'))
    assert_true(check('123|122'))
    assert_true(check('sdfsdf|122'))
    assert_true(check('|122'))
    assert_true(check('..|122'))
    assert_true(check('..122'))
    assert_true(check('adfsdf..122'))
    assert_true(check('123|||'))
    
    assert_false(check('가'))
    assert_false(check('+123-=-='))
    assert_false(check('/--*-*'))
    assert_false(check('()'))
    assert_false(check('123|---'))
    
    # check whether given text matches with given pattern. 
    assert_true(exact_match('1', '1')) # 20
    assert_true(exact_match('.', '1'))
    assert_true(exact_match('1', '1'))
    assert_true(exact_match('1|2', '1'))
    assert_true(exact_match('1|2', '2'))
    assert_true(exact_match('.|2', '1'))
    assert_true(exact_match('|2', ''))
    assert_true(exact_match('\.', '.'))
    
    assert_false(exact_match('..', '1'))
    assert_false(exact_match('..', '1'))
    assert_false(exact_match('..|2', '1'))
    assert_false(exact_match('..|.2', '1'))
    assert_false(exact_match('..|ab', '1'))
    
    #assert_error(exact_match(1, 2), ValueError)
    
    
    
if __name__ == '__main__':
    test()