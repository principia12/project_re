def check_date(text):
    for char in text:
        assert char in ['0', '1', '2', '3', '4', \
            '5', '6', '7', '8', '9',]
    assert len(char) == 8
    
def check_numeric(char):
    assert char in ['0', '1', '2', '3', '4', \
        '5', '6', '7', '8', '9',]

def check_date(text):
    for char in text:
        assert check_numeric(char)

def check_numeric(char, start, end):
    assert char in [str(e) for e in range(start, end+1)]
    
def check_date(text):
    assert check_numeric(text[0], 0, 9)
    assert check_numeric(text[1], 0, 9)
    assert check_numeric(text[2], 0, 9)
    assert check_numeric(text[3], 0, 9)
    if check_numeric(text[4], 0, 0):
        assert check_numeric(text[5], 0, 9)
    elif check_numeric(text[4], 1, 1):
        assert check_numeric(text[5], 0, 1)
    assert check_numeric(text[6], 0, 3)
    if check_numeric(text[6], 0, 2):
        assert check_numeric(text[7], 0, 9)
    elif check_numeric(text[4], 3, 3):
        assert check_numeric(text[7], 0, 9)
    

def null():
    for char in text[:4]:
        assert char in ['0', '1', '2', '3', '4', \
            '5', '6', '7', '8', '9',]
    for char in text[4:6]:
        assert char in ['0', '1', '2', '3', '4', \
            '5', '6', '7', '8', '9',]