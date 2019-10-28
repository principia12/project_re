import sys 
import os 
from pprint import pprint 

def testing(func):
    def execute(*arg, **kargs):
        res = func(*arg, **kargs)
        
        testcases, right, wrong, wrong_cases = test_stats
        print('---------------------------')
        print('test summary')
        print('---------------------------')
        print('Total %d testcases.'%testcases)
        print('%d out of %d right, %.2f percent.'%(right, testcases, round(100.0*right/testcases, 2)))
        print('wrong cases;')
        pprint(wrong_cases)
        
        
        return res
    
    return execute

test_stats = [0, 0, 0, []]

def assert_condition(cond, lst = test_stats):
    def f(*arg, **kargs):
        lst[0] += 1
        if cond(*arg, **kargs):
            lst[1] += 1
        else:
            lst[2] += 1 
            lst[3].append((lst[0]))
    
    return f 
    
def check_err(x, err):
    try:
        x
        return False 
    except err:
        return True 
    except :
        return False 
    
    
assert_true = assert_condition(lambda x : x is True)
assert_false = assert_condition(lambda x : x is False)
assert_eq = assert_condition(lambda x, y : x == y)
assert_member = assert_condition(lambda x : x in globals())
assert_error = assert_condition(lambda x, y : x == y)


class NoModuleSpecifiedError(Exception):
    pass 

if len(sys.argv) < 2:
    raise NoModuleSpecifiedError('Specify target directory to test.')
    
module_name = sys.argv[1]

if module_name not in os.listdir():
    raise NoModuleSpecifiedError('Target directory not in root directory; %s not in root.'%module_name)

module_name = sys.argv[1]
exec('from %s.main import *'%module_name)