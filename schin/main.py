
numbers = '1234567890'
alphabets = 'qwertyuiopasdfghjklzxcvbnm'
wildcard = '.'
operator_or = '|'
backslash = '\\'

def check(pattern):
    if not isinstance(pattern, str):
        return False
    tmp = [True]
    for idx, char in enumerate(pattern):
        if char in alphabets + numbers + wildcard:
            tmp.append(tmp[-1])
        elif char == backslash:
            tmp.append(pattern[idx+1] == '.')
        elif char == operator_or:
            if any([not e for e in tmp]):
                return False 
            else:
                tmp = [True]
        else:
            return False 
    return tmp != [] and tmp[-1] 

def exact_match(pattern, text):
    if check(pattern):
        pattern = pattern.replace('\\', '')
        if '|' in pattern:
            patterns = pattern.split('|')
            
            
            return any([exact_match(p, text) for p in patterns])
        else:
            return all([x == y or (x == '.' and y in alphabets + numbers + wildcard) for x, y in zip(pattern, text)]) and len(pattern) == len(text)
                    
    
    return ValueError
    