
# 일단 숫자만 8자리 맞추는 파이 만들자
# 다음은 문자 등등하기
numbers = '12345678'
alpa = 'qwertyuiopasdfghjklzxcvbn'
#numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

class numberError(Exception):
    pass
class alpaError(Exception):
    pass

class PatternCat:
    #영어와 숫자를 분리하는 방법?
    def __init__(self, x):
        self.x = x

    def number_true(self):
        for number in self.x:
            try: 
                assert number in numbers

            except: 
                raise numberError()

            try:
                 assert number in alpa

            except: 
                raise alpaError()
            
           # assert number in numbers

    
     

class Cat:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printcat(self):
        print(self.name, self.age)